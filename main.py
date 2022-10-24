from typing import List
import pygame
import numpy as np
import wireframe_library as wl

wireframe_select = int(input("What wireframe should be rendered(0: Cube, 1: LOL)? "))
wireframe = wl.all_wireframes[wireframe_select]

vertex_positions = wireframe[0]
edge_table = wireframe[1]

rotation_matrix_x = np.array((  (1, 0, 0),
                                (0, np.cos(0.01), -np.sin(0.01)),
                                (0, np.sin(0.01), np.cos(0.01))))

rotation_matrix_y = np.array((  (np.cos(0.01), 0, np.sin(0.01)),
                                (0, 1, 0),
                                (-np.sin(0.01), 0, np.cos(0.01))))

rotation_matrix_z = np.array((  (np.cos(0.01), -np.sin(0.01), 0),
                                (np.sin(0.01), np.cos(0.01), 0),
                                (0, 0, 1)))

rotation_matricies = (  rotation_matrix_x,
                        rotation_matrix_y,
                        rotation_matrix_z)

pygame.init()
screen_size = (640, 480)
screen_center = (screen_size[0]//2, screen_size[1]//2)
screen = pygame.display.set_mode(screen_size)
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

focal_length = 5

def rotate_vertex_positions(vertex_positions: List, rotation_axis_index: int) -> List:
    #Around what axis the cube should rotate
    vertex_positions = np.dot(vertex_positions, rotation_matricies[rotation_axis_index])
    return vertex_positions

def project_vertex_position(vertex: List) -> List:
    projected_x_position = (focal_length * vertex[0]) / (focal_length + vertex[2])
    projected_y_position = (focal_length * vertex[1]) / (focal_length + vertex[2])
    return [projected_x_position, projected_y_position]

def convert_projected_position_to_screen_coordinates(projected_vertex: List) -> List:
    screen_x_coordinates = projected_vertex[0]*50 + screen_center[0]
    screen_y_coordinates = projected_vertex[1]*50 + screen_center[1]
    return [screen_x_coordinates, screen_y_coordinates]

def loop(rotation_axis_index: int) -> None:
    global vertex_positions
    if auto_rotate:
        #Rotate around the y-Axis by default
        vertex_positions = rotate_vertex_positions(vertex_positions, 1)
    if not auto_rotate and rotation_axis_index != None:
        vertex_positions = rotate_vertex_positions(vertex_positions, rotation_axis_index)

    vertex_screen_positions = []
    screen.fill((255, 255, 255))

    for vertex in vertex_positions:
        vertex_screen_positions.append(convert_projected_position_to_screen_coordinates(project_vertex_position(vertex)))
        pygame.draw.circle(screen, (0, 0, 0), vertex_screen_positions[-1], 2, 0)

    for edge in edge_table:
        pygame.draw.line(screen, (0, 0, 0), vertex_screen_positions[edge[0]], vertex_screen_positions[edge[1]], 2)

def poll_input_keys() -> int:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        return 0
    if keys[pygame.K_d]:
        return 1
    if keys[pygame.K_e]:
        return 2
    else:
        return None



active = True
auto_rotate = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == 32 and auto_rotate:
                auto_rotate = False
            elif event.key == 32 and not auto_rotate:
                auto_rotate = True

    rotation_axis_index = poll_input_keys()
    #print(rotation_axis_index)
    loop(rotation_axis_index)    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()