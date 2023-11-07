from Structures.value_and_bits import ValueAndBitsList


MAX_DISTANCE = 32768
OUT_BUD_SIZE = 8192

length_data = ValueAndBitsList.create_list(
    (3, 0), (4, 0), (5, 0), (6, 0),
    (7, 0), (8, 0), (9, 0), (10, 0),
    (11, 1), (13, 1), (15, 1),
    (17, 1), (19, 2), (23, 2),
    (27, 2), (31, 2), (35, 3),
    (43, 3), (51, 3), (59, 3),
    (67, 4), (83, 4), (99, 4),
    (115, 4), (131, 5), (163, 5),
    (195, 5), (227, 5), (258, 0)
)

dist_data = ValueAndBitsList.create_list(
    (1, 0), (2, 0), (3, 0), (4, 0),
    (5, 1), (7, 1), (9, 2), (13, 2),
    (17, 3), (25, 3), (33, 4), (49, 4),
    (65, 5), (97, 5), (129, 6),
    (193, 6), (257, 7), (385, 7),
    (513, 8), (769, 8), (1025, 9),
    (1537, 9), (2049, 10), (3073, 10),
    (4097, 11), (6145, 11), (8193, 12),
    (12289, 12), (16385, 13),
    (24577, 13)
)
