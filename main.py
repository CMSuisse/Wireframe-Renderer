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

rotation_axis_select = int(input("Around which axis should the wireframe rotate (0: x, 1: y, 2: z)? "))
rotation_axis = rotation_matricies[rotation_axis_select]

pygame.init()
screen_size = (640, 480)
screen_center = (screen_size[0]//2, screen_size[1]//2)
screen = pygame.display.set_mode(screen_size)
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

focal_length = 5

def rotate_vertex_positions(vertex_positions: List) -> List:
    #Around what axis the cube should rotate
    vertex_positions = np.dot(vertex_positions, rotation_axis)
    return vertex_positions

def project_vertex_position(vertex: List) -> List:
    projected_x_position = (focal_length * vertex[0]) / (focal_length + vertex[2])
    projected_y_position = (focal_length * vertex[1]) / (focal_length + vertex[2])
    return [projected_x_position, projected_y_position]

def convert_projected_position_to_screen_coordinates(projected_vertex: List) -> List:
    screen_x_coordinates = projected_vertex[0]*50 + screen_center[0]
    screen_y_coordinates = projected_vertex[1]*50 + screen_center[1]
    return [screen_x_coordinates, screen_y_coordinates]

def loop() -> None:
    global vertex_positions
    vertex_positions = rotate_vertex_positions(vertex_positions)
    vertex_screen_positions = []
    screen.fill((255, 255, 255))

    for vertex in vertex_positions:
        vertex_screen_positions.append(convert_projected_position_to_screen_coordinates(project_vertex_position(vertex)))
        pygame.draw.circle(screen, (0, 0, 0), vertex_screen_positions[-1], 2, 0)

    for edge in edge_table:
        pygame.draw.line(screen, (0, 0, 0), vertex_screen_positions[edge[0]], vertex_screen_positions[edge[1]], 2)


active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    
    loop()    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()