import numpy as np

cube_vertex_positions = np.array(((-1, -1, 1),
                                (1, -1, 1), 
                                (-1, 1, 1), 
                                (1, 1, 1), 
                                (-1, -1, -1), 
                                (1, -1, -1), 
                                (-1, 1, -1), 
                                (1, 1, -1)))
                                                
cube_edge_table = np.array(( (0, 1),
                            (0, 2),
                            (2, 3),
                            (3, 1),
                            (4, 5),
                            (4, 6),
                            (6, 7),
                            (7, 5),
                            (0, 4),
                            (2, 6),
                            (3, 7),
                            (1, 5)))
cube = np.array((cube_vertex_positions, cube_edge_table), dtype=np.ndarray)

lol_vertex_positions = np.array(((-.5, 1, 0),
                                (.5, 1, 0),
                                (-.5, -1, 0),
                                (.5, -1, 0),
                                
                                (-1, 1, 0),
                                (-1.5, 1, 0),
                                (-1.5, -1, 0),
                                
                                (2, 1, 0),
                                (1.5, 1, 0),
                                (1.5, -1, 0)))
                            
lol_edge_table = np.array(( (0, 1),
                            (0, 2),
                            (1, 3),
                            (2, 3),
                            (4, 5),
                            (5,6),
                            (7, 8),
                            (8, 9)))

lol = np.array((lol_vertex_positions, lol_edge_table), dtype = np.ndarray)

all_wireframes = (cube, lol)