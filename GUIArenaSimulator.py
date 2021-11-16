import math
import sys
sys.path.insert(1, "../pythonSimulator")
import NDIImageSender
import ArenaSimulator
import ConfigReader
import RESTApiClient

# read some configs from the config file
config_file = "../pythonSimulator/robot.cfg"
config_reader = ConfigReader.ConfigReader(config_file)
window_width = int(config_reader.get_value_string("simulation.window_width"))
window_height = int(config_reader.get_value_string("simulation.window_height"))
x_lb = ArenaSimulator.str2list(config_reader.get_value_string("system.states.first_symbol"))
x_ub = ArenaSimulator.str2list(config_reader.get_value_string("system.states.last_symbol"))
x_eta = ArenaSimulator.str2list(config_reader.get_value_string("system.states.quantizers"))
path_tail_length = int(config_reader.get_value_string("simulation.path_tail_length"))

# the NDI interface
ndiImgSender = NDIImageSender.NDIImageSender(b'My_PNG', 10)


# the REST client
objects_server_url = config_reader.get_value_string("simulation.objects_server_url")
rest_client = RESTApiClient.RESTApiClient(objects_server_url)


def translate_norm_to_arena(norm):
    arena_x = (norm[0])*(window_width/(x_ub[0] - x_lb[0]))
    arena_y = (norm[1])*(window_height/(x_ub[1] - x_lb[1]))
    return [arena_x, arena_y]

def translate_state_to_arena(state):
    arena_x = (state[0] - x_lb[0] + x_eta[0]/2)*(window_width/(x_ub[0] - x_lb[0] + x_eta[0]))    
    arena_y = (state[1] - x_lb[1] + x_eta[1]/2)*(window_height/(x_ub[1] - x_lb[1] + x_eta[1]))
    return [arena_x, arena_y]

def shift_and_add(lst, itm):
    out = lst
    lst_len = len(lst)
    
    if lst_len == 0:
        return out

    for i in range(lst_len-1):
        lst[i] = lst[i+1]
    lst[len(lst)-1] = itm

    return out

path_tail = [None]*path_tail_length
DR_last_state = None
def after_draw(arcade):
    global path_tail
    global DR_last_state

    # get arena objects
    try:
        response = rest_client.restGETjson()
        items = response.items()
    except:
        items = []

    # item[0] = name, item[1] = "untracked" or will be list of values
    for item in items:
        is_passed = False
        if item[1] != "untracked":        
            values = item[1].split(',')
            x_val = float(values[1])
            y_val = float(values[2])
            width = float(values[5])
            height = float(values[6])

            if "DeepRacer" in item[0]: # is a DeepRacer robot
                angle = (-float(values[3])*180/math.pi + -90)
                color = arcade.color.BLUE    
            elif "Target" in item[0]: # is a target
                angle = 0
                color = arcade.color.APPLE_GREEN
            elif "Obstacle" in item[0]: # is an obstacle
                angle = 0
                color = arcade.color.CRIMSON
            else:
                is_passed = True
                pass
        else:
            is_passed = True
            pass

        # draw_rectangle_filled(x_position, y_position, width, height, color)
        if is_passed == False:
            [x,y] = translate_state_to_arena([x_val, y_val])
            [width, height] = translate_norm_to_arena([width, height])
            arcade.draw_rectangle_filled(x, y, width, height, color, angle)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

            if "DeepRacer" in item[0]:
                if DR_last_state == None:
                    DR_last_state = [x,y]
                else:
                    path_tail = shift_and_add(path_tail,[DR_last_state, [x,y]])
                    DR_last_state = [x,y]

    # draw tail
    for line in path_tail:
        if line != None:
            arcade.draw_line(line[0][0], line[0][1], line[1][0], line[1][1], arcade.color.BLUE, 5)

    image_bytes = arcade.get_image().tobytes()
    width = arcade.get_image().width
    height = arcade.get_image().height
    ndiImgSender.send_image(image_bytes, width, height)

    # for testing
    return [image_bytes, width, height]

#if __name__ == "__main__":
def test_get_simulator():
    ArenaSimulator.ArenaSimulator(
        None,         	# dynamics function of the model
        config_file,    # the config file oof the problem
        after_draw
    ).start()