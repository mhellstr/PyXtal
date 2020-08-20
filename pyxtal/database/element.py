"""
Module for handling atomic elements.
"""
from numpy import vectorize


class Element:
    """
    Class for storing and accessing atomic elements. 

    Args:
        input_value: The atomic number, symbol, or name of the element
    """

    def __init__(self, input_value):
        self.input = input_value

        # list with atomic number z, short name, full name, valence,
        # valence electrons, covalent radius, vdW radius, metallic radius
        self.elements_list = [
            (1, "H", "Hydrogen", 1.0, 1, 0.31, 1.20, None),
            (2, "He", "Helium", 0.5, 2, 0.28, 1.40, None),
            (3, "Li", "Lithium", 1.0, 1, 1.28, 1.82, 1.52),
            (4, "Be", "Beryllium", 2.0, 2, 0.96, 1.53, 1.12),
            (5, "B", "Boron", 3.0, 3, 0.84, 1.92, None),
            (6, "C", "Carbon", 4.0, 4, 0.78, 1.70, None),
            (7, "N", "Nitrogen", 3.0, 5, 0.78, 1.55, None),
            (8, "O", "Oxygen", 2.0, 6, 0.70, 1.52, None),
            (9, "F", "Fluorine", 1.0, 7, 0.57, 1.47, None),
            (10, "Ne", "Neon", 0.5, 8, 0.58, 1.54, None),
            (11, "Na", "Sodium", 1.0, 1, 1.66, 2.27, 1.86),
            (12, "Mg", "Magnesium", 2.0, 2, 1.41, 1.73, 1.60),
            (13, "Al", "Aluminium", 3.0, 3, 1.21, 1.84, 1.43),
            (14, "Si", "Silicon", 4.0, 4, 1.11, 2.10, None),
            (15, "P", "Phosphorus", 3.0, 5, 1.07, 1.80, None),
            (16, "S", "Sulfur", 2.0, 6, 1.25, 1.80, None),
            (17, "Cl", "Chlorine", 1.0, 7, 1.02, 1.75, None),
            (18, "Ar", "Argon", 0.5, 8, 1.06, 1.88, None),
            (19, "K", "Potassium", 1.0, 1, 2.03, 2.75, 2.27),
            (20, "Ca", "Calcium", 2.0, 2, 1.76, 2.31, 1.97),
            (21, "Sc", "Scandium", 3.0, 3, 1.70, 2.11, 1.62),
            (22, "Ti", "Titanium", 4.0, 4, 1.60, 2.00, 1.47),
            (23, "V", "Vanadium", 4.0, 5, 1.53, 2.00, 1.34),
            (24, "Cr", "Chromium", 3.0, 6, 1.39, 2.00, 1.28),
            (25, "Mn", "Manganese", 4.0, 5, 1.39, 2.00, 1.27),
            (26, "Fe", "Iron", 3.0, 3, 1.32, 2.00, 1.26),
            (27, "Co", "Cobalt", 3.0, 3, 1.26, 2.00, 1.25),
            (28, "Ni", "Nickel", 2.0, 3, 1.24, 1.63, 1.24),
            (29, "Cu", "Copper", 2.0, 2, 1.32, 1.40, 1.28),
            (30, "Zn", "Zinc", 2.0, 2, 1.22, 1.39, 1.34),
            (31, "Ga", "Gallium", 3.0, 3, 1.22, 1.87, 1.35),
            (32, "Ge", "Germanium", 4.0, 4, 1.20, 2.11, None),
            (33, "As", "Arsenic", 3.0, 5, 1.19, 1.85, None),
            (34, "Se", "Selenium", 2.0, 6, 1.20, 1.90, None),
            (35, "Br", "Bromine", 1.0, 7, 1.20, 1.85, None),
            (36, "Kr", "Krypton", 0.5, 8, 1.16, 2.02, None),
            (37, "Rb", "Rubidium", 1.0, 1, 2.20, 3.03, 2.48),
            (38, "Sr", "Strontium", 2.0, 2, 1.95, 2.49, 2.15),
            (39, "Y", "Yttrium", 3.0, 3, 1.90, 2.00, 1.80),
            (40, "Zr", "Zirconium", 4.0, 4, 1.75, 2.00, 1.60),
            (41, "Nb", "Niobium", 5.0, 5, 1.64, 2.00, 1.46),
            (42, "Mo", "Molybdenum", 4.0, 6, 1.54, 2.00, 1.39),
            (43, "Tc", "Technetium", 4.0, 5, 1.47, 2.00, 1.36),
            (44, "Ru", "Ruthenium", 4.0, 3, 1.46, 2.00, 1.34),
            (45, "Rh", "Rhodium", 4.0, 3, 1.42, 1.63, 1.34),
            (46, "Pd", "Palladium", 4.0, 3, 1.39, 1.72, 1.37),
            (47, "Ag", "Silver", 1.0, 2, 1.45, 1.58, 1.44),
            (48, "Cd", "Cadmium", 2.0, 2, 1.44, 1.93, 1.51),
            (49, "In", "Indium", 3.0, 3, 1.42, 2.17, 1.67),
            (50, "Sn", "Tin", 4.0, 4, 1.39, 2.06, None),
            (51, "Sb", "Antimony", 3.0, 5, 1.39, 2.06, None),
            (52, "Te", "Tellurium", 2.0, 6, 1.38, 2.06, None),
            (53, "I", "Iodine", 1.0, 7, 1.39, 1.98, None),
            (54, "Xe", "Xenon", 0.5, 8, 1.40, 2.16, None),
            (55, "Cs", "Caesium", 1.0, 1, 2.44, 3.43, 2.65),
            (56, "Ba", "Barium", 2.0, 2, 2.15, 2.68, 2.22),
            (57, "La", "Lanthanum", 3.0, 3, 2.07, 2.10, 1.87),
            (58, "Ce", "Cerium", 4.0, 3, 2.04, 2.10, 1.818),
            (59, "Pr", "Praseodymium", 3.0, 3, 2.03, 2.10, 1.824),
            (60, "Nd", "Neodymium", 3.0, 3, 2.01, 2.10, 1.814),
            (61, "Pm", "Promethium", 3.0, 3, 1.99, 2.10, 1.834),
            (62, "Sm", "Samarium", 3.0, 3, 1.98, 2.10, 1.804),
            (63, "Eu", "Europium", 3.0, 3, 1.98, 2.10, 1.804),
            (64, "Gd", "Gadolinium", 3.0, 3, 1.96, 2.10, 1.804),
            (65, "Tb", "Terbium", 3.0, 3, 1.94, 2.10, 1.773),
            (66, "Dy", "Dysprosium", 3.0, 3, 1.92, 2.10, 1.781),
            (67, "Ho", "Holmium", 3.0, 3, 1.92, 2.10, 1.762),
            (68, "Er", "Erbium", 3.0, 3, 1.89, 2.10, 1.761),
            (69, "Tm", "Thulium", 3.0, 3, 1.90, 2.10, 1.759),
            (70, "Yb", "Ytterbium", 3.0, 3, 1.87, 2.10, 1.76),
            (71, "Lu", "Lutetium", 3.0, 3, 1.87, 2.10, 1.738),
            (72, "Hf", "Hafnium", 4.0, 3, 1.75, 2.10, 1.59),
            (73, "Ta", "Tantalum", 5.0, 3, 1.70, 2.10, 1.46),
            (74, "W", "Tungsten", 4.0, 3, 1.62, 2.10, 1.39),
            (75, "Re", "Rhenium", 4.0, 3, 1.51, 2.10, 1.37),
            (76, "Os", "Osmium", 4.0, 3, 1.44, 2.10, 1.35),
            (77, "Ir", "Iridium", 4.0, 3, 1.41, 2.10, 1.355),
            (78, "Pt", "Platinum", 4.0, 3, 1.36, 1.75, 1.385),
            (79, "Au", "Gold", 1.0, 3, 1.36, 1.66, 1.44),
            (80, "Hg", "Mercury", 2.0, 3, 1.32, 1.55, 1.51),
            (81, "Tl", "Thallium", 3.0, 3, 1.45, 1.96, 1.70),
            (82, "Pb", "Lead", 4.0, 4, 1.46, 2.02, None),
            (83, "Bi", "Bismuth", 3.0, 5, 1.48, 2.07, None),
            (84, "Po", "Polonium", 2.0, 6, 1.40, 1.97, None),
            (85, "At", "Astatine", 1.0, 7, 1.50, 2.02, None),
            (86, "Rn", "Radon", 0.5, 8, 1.50, 2.20, None),
            (87, "Fr", "Francium", 1.0, 1, 2.60, 3.48, None),
            (88, "Ra", "Radium", 2.0, 2, 2.21, 2.83, None),
            (89, "Ac", "Actinium", 3.0, 3, 2.15, 2.20, None),
            (90, "Th", "Thorium", 4.0, 3, 2.06, 2.20, 1.79),
            (91, "Pa", "Protactinium", 4.0, 3, 2.00, 2.20, 1.63),
            (92, "U", "Uranium", 4.0, 3, 1.96, 2.20, 1.56),
            (93, "Np", "Neptunium", 4.0, 3, 1.90, 2.20, 1.55),
            (94, "Pu", "Plutonium", 4.0, 3, 1.87, 2.20, 1.59),
            (95, "Am", "Americium", 4.0, 3, 1.80, 2.20, 1.73),
            (96, "Cm", "Curium", 4.0, 3, 1.69, 2.20, 1.74),
            (97, "Bk", "Berkelium", 4.0, 3, None, None, 1.70),
            (98, "Cf", "Californium", 4.0, 3, None, None, 1.86),
            (99, "Es", "Einsteinium", 4.0, 3, None, None, 1.86),
            (100, "Fm", "Fermium", 4.0, 3, None, None, None),
            (101, "Md", "Mendelevium", 4.0, 3, None, None, None),
            (102, "No", "Nobelium", 4.0, 3, None, None, None),
            (103, "Lr", "Lawrencium", 4.0, 3, None, None, None),
            (104, "Rf", "Rutherfordium", 4.0, 3, None, None, None),
            (105, "Db", "Dubnium", 2.0, 3, None, None, None),
        ]
        """A list of atomic numbers, symbols, names, and other information, up
        to atomic number 105"""

        # scatter factor
        self.sf = [
            [0.493, 0.323, 0.140, 0.041, 10.511, 26.126, 3.142, 57.800, 0.003],
            [0.873, 0.631, 0.311, 0.178, 9.104, 3.357, 22.928, 0.982, 0.006],
            [1.128, 0.751, 0.618, 0.465, 3.955, 1.052, 85.391, 168.261, 0.038],
            [1.592, 1.128, 0.539, 0.703, 43.643, 1.862, 103.483, 0.542, 0.038],
            [2.055, 1.333, 1.098, 0.707, 23.219, 1.021, 60.350, 0.140, -0.193],
            [2.310, 1.020, 1.589, 0.865, 20.844, 10.208, 0.569, 51.651, 0.216],
            [12.213, 3.132, 2.013, 1.166, 0.006, 9.893, 28.997, 0.583, -11.529],
            [3.049, 2.287, 1.546, 0.867, 13.277, 5.701, 0.324, 32.909, 0.251],
            [3.539, 2.641, 1.517, 1.024, 10.283, 4.294, 0.262, 26.148, 0.278],
            [3.955, 3.112, 1.455, 1.125, 8.404, 3.426, 0.231, 21.718, 0.352],
            [4.763, 3.174, 1.267, 1.113, 3.285, 8.842, 0.314, 129.424, 0.676],
            [5.420, 2.174, 1.227, 2.307, 2.828, 79.261, 0.381, 7.194, 0.858],
            [6.420, 1.900, 1.594, 1.965, 3.039, 0.743, 31.547, 85.089, 1.115],
            [6.292, 3.035, 1.989, 1.541, 2.439, 32.334, 0.678, 81.694, 1.141],
            [6.435, 4.179, 1.780, 1.491, 1.907, 27.157, 0.526, 68.164, 1.115],
            [6.905, 5.203, 1.438, 1.586, 1.468, 22.215, 0.254, 56.172, 0.867],
            [11.460, 7.196, 6.256, 1.645, 0.010, 1.166, 18.519, 47.778, -9.557],
            [7.484, 6.772, 0.654, 1.644, 0.907, 14.841, 43.898, 33.393, 1.444],
            [8.219, 7.440, 1.052, 0.866, 12.795, 0.775, 213.187, 41.684, 1.423],
            [8.627, 7.387, 1.590, 1.021, 10.442, 0.660, 85.748, 178.437, 1.375],
            [9.189, 7.368, 1.641, 1.468, 9.021, 0.573, 136.108, 51.353, 1.333],
            [9.759, 7.356, 1.699, 1.902, 7.851, 0.500, 35.634, 116.105, 1.281],
            [10.297, 7.351, 2.070, 2.057, 6.866, 0.438, 26.894, 102.478, 1.220],
            [10.641, 7.354, 3.324, 1.492, 6.104, 0.392, 20.263, 98.740, 1.183],
            [11.282, 7.357, 3.019, 2.244, 5.341, 0.343, 17.867, 83.754, 1.090],
            [11.769, 7.357, 3.522, 2.305, 4.761, 0.307, 15.354, 76.881, 1.037],
            [12.284, 7.341, 4.003, 2.349, 4.279, 0.278, 13.536, 71.169, 1.012],
            [12.838, 7.292, 4.444, 2.380, 3.878, 0.257, 12.176, 66.342, 1.034],
            [13.338, 7.168, 5.616, 1.673, 3.583, 0.247, 11.397, 64.831, 1.191],
            [14.074, 7.032, 5.165, 2.410, 3.266, 0.233, 10.316, 58.710, 1.304],
            [15.235, 6.701, 4.359, 2.962, 3.067, 0.241, 10.781, 61.414, 1.719],
            [16.082, 6.375, 3.707, 3.683, 2.851, 0.252, 11.447, 54.763, 2.131],
            [16.672, 6.070, 3.431, 4.278, 2.635, 0.265, 12.948, 47.797, 2.531],
            [17.001, 5.820, 3.973, 4.354, 2.410, 0.273, 15.237, 43.816, 2.841],
            [17.179, 5.236, 5.638, 3.985, 2.172, 16.580, 0.261, 41.433, 2.956],
            [17.355, 6.729, 5.549, 3.537, 1.938, 16.562, 0.226, 39.397, 2.825],
            [17.178, 9.644, 5.140, 1.529, 1.789, 17.315, 0.275, 164.934, 3.487],
            [17.566, 9.818, 5.422, 2.669, 1.556, 14.099, 0.166, 132.376, 2.506],
            [17.776, 10.295, 5.726, 3.266, 1.403, 12.801, 0.261, 104.354, 1.912],
            [17.876, 10.948, 5.417, 3.657, 1.276, 11.916, 0.118, 87.663, 2.069],
            [17.614, 12.014, 4.042, 3.533, 1.189, 11.766, 0.205, 69.796, 3.756],
            [3.703, 17.236, 12.888, 3.743, 0.277, 1.096, 11.004, 61.658, 4.387],
            [19.130, 11.095, 4.649, 2.713, 0.864, 8.145, 21.571, 86.847, 5.404],
            [19.267, 12.918, 4.863, 1.568, 0.809, 8.435, 24.800, 94.293, 5.379],
            [19.296, 14.350, 4.734, 1.289, 0.752, 8.218, 25.875, 98.606, 5.328],
            [19.332, 15.502, 5.295, 0.606, 0.699, 7.989, 25.205, 76.899, 5.266],
            [19.281, 16.688, 4.805, 1.046, 0.645, 7.473, 24.660, 99.816, 5.179],
            [19.221, 17.644, 4.461, 1.603, 0.595, 6.909, 24.701, 87.482, 5.069],
            [19.162, 18.560, 4.295, 2.040, 0.548, 6.378, 25.850, 92.803, 4.939],
            [19.189, 19.101, 4.458, 2.466, 5.830, 0.503, 26.891, 83.957, 4.782],
            [19.642, 19.045, 5.037, 2.683, 5.303, 0.461, 27.907, 75.283, 4.591],
            [19.964, 19.014, 6.145, 2.524, 4.817, 0.421, 28.528, 70.840, 4.352],
            [20.147, 18.995, 7.514, 2.273, 4.347, 0.381, 27.766, 66.878, 4.071],
            [20.293, 19.030, 8.977, 1.990, 3.928, 0.344, 26.466, 64.266, 3.712],
            [20.389, 19.106, 10.662, 1.495, 3.569, 0.311, 24.388, 213.904, 3.335],
            [20.336, 19.297, 10.888, 2.696, 3.216, 0.276, 20.207, 167.202, 2.773],
            [20.578, 19.599, 11.373, 3.287, 2.948, 0.244, 18.773, 133.124, 2.147],
            [21.167, 19.770, 11.851, 3.330, 2.812, 0.227, 17.608, 127.113, 1.863],
            [22.044, 19.670, 12.386, 2.824, 2.774, 0.222, 16.767, 143.644, 2.058],
            [22.684, 19.685, 12.774, 2.851, 2.662, 0.211, 15.885, 137.903, 1.985],
            [23.340, 19.610, 13.123, 2.875, 2.563, 0.202, 15.101, 132.721, 2.029],
            [24.004, 19.426, 13.440, 2.896, 2.473, 0.196, 14.400, 128.007, 2.210],
            [24.627, 19.089, 13.760, 2.293, 2.388, 0.194, 13.755, 123.174, 2.575],
            [25.071, 19.080, 13.852, 3.545, 2.253, 0.182, 12.933, 101.398, 2.420],
            [25.898, 18.219, 14.317, 2.954, 2.243, 0.196, 12.665, 115.362, 3.583],
            [26.507, 17.638, 14.560, 2.966, 2.180, 0.202, 12.190, 111.874, 4.297],
            [26.905, 17.294, 14.558, 3.638, 2.071, 0.198, 11.441, 92.657, 4.568],
            [27.656, 16.428, 14.978, 2.982, 2.074, 0.224, 11.360, 105.703, 5.920],
            [28.182, 15.885, 15.154, 2.987, 2.029, 0.239, 10.998, 102.961, 6.756],
            [28.664, 15.434, 15.309, 2.990, 1.989, 0.257, 10.665, 100.417, 7.567],
            [28.948, 15.221, 15.100, 3.716, 1.902, 9.985, 0.261, 84.330, 7.976],
            [29.144, 15.173, 14.759, 4.300, 1.833, 9.600, 0.275, 72.029, 8.582],
            [29.202, 15.229, 14.514, 4.765, 1.773, 9.370, 0.296, 63.364, 9.244],
            [0.000, 0.000, 0.000, 0.000, 1.722, 9.231, 0.323, 57.725, 9.858],
            [28.762, 15.719, 14.556, 5.442, 1.672, 9.092, 0.350, 52.086, 10.472],
            [28.189, 16.155, 14.931, 5.676, 1.629, 8.979, 0.383, 48.165, 11.000],
            [27.305, 16.730, 15.611, 5.834, 1.593, 8.866, 0.418, 45.001, 11.472],
            [27.006, 17.764, 15.713, 5.784, 1.513, 8.812, 0.425, 38.610, 11.688],
            [16.882, 18.591, 25.558, 5.860, 0.461, 8.622, 1.483, 36.396, 12.066],
            [20.681, 19.042, 21.657, 5.968, 0.545, 8.448, 1.573, 38.325, 12.609],
            [27.545, 19.158, 15.538, 5.526, 0.655, 8.708, 1.963, 45.815, 13.175],
            [31.062, 13.064, 18.442, 5.970, 0.690, 2.358, 8.618, 47.258, 13.412],
            [33.369, 12.951, 16.588, 6.469, 0.704, 2.924, 8.794, 48.009, 13.578],
            [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
            [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
            [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
            [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
            [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
            [35.660, 23.103, 12.598, 4.087, 0.589, 3.652, 18.599, 117.020, 13.527],
            [35.564, 23.422, 12.747, 4.807, 0.563, 3.462, 17.831, 99.172, 13.431],
            [35.885, 23.295, 14.189, 4.173, 0.548, 3.415, 16.924, 105.251, 13.429],
            [0.000, 0.000, 0.000, 0.000, 0.530, 3.335, 16.143, 101.371, 13.393],
            [36.187, 23.596, 15.640, 4.186, 0.512, 3.254, 15.362, 97.491, 13.357],
            [36.526, 23.808, 16.771, 3.479, 0.499, 3.264, 14.946, 105.980, 13.381],
        ]
        """A list of scatter factors for the elements"""

        self.z = None
        """atomic number"""
        self.short_name = None
        """atomic symbol"""
        self.long_name = None
        """atomic name"""
        self.valence = None
        """valence value"""
        self.valence_electrons = None
        """number of valence electrons"""
        self.covalent_radius = None
        """atomic radius used for distance checking within crystals"""
        self.vdw_radius = None
        """atomic radius used for volume estimation within crystals"""
        self.metallic_radius = None
        """atomic radius used for distance checking within metallic crystals"""

        pos = None

        try:
            int(self.input)
            self.z = self.input

            for i, el in enumerate(self.elements_list):
                if el[0] == self.z:
                    pos = i
                    self.short_name = el[1]
                    self.long_name = el[2]
                    break
        except ValueError:
            self.short_name = self.input
            for i, el in enumerate(self.elements_list):
                if el[1] == self.short_name:
                    pos = i
                    self.z = el[0]
                    self.long_name = el[2]
                    break

            if not self.z:
                self.short_name = None
                self.long_name = self.input
                for i, el in enumerate(self.elements_list):
                    if el[2] == self.long_name:
                        pos = i
                        self.z = el[0]
                        self.short_name = el[1]
                        break
                if not self.z:
                    self.long_name = None

        if pos is not None:
            self.valence = self.elements_list[pos][3]
            self.valence_electrons = self.elements_list[pos][4]
            self.covalent_radius = self.elements_list[pos][5]
            self.vdw_radius = self.elements_list[pos][6]
            self.metallic_radius = self.elements_list[pos][7]
            self.scatter = self.sf[pos]

    def get_all(self, pos):
        """
        Return all [pos] elements in the full element list
        
        Args:
            pos: the index of the elements to retrieve
        
        Returns:
            a list containing only the [pos] elements of self.elements_list
        """
        els = []
        for el in self.elements_list:
            els.append(el[pos])
        return els

    def get_sf(self, pos):
        """
        Get the scattering factor for an element.
        
        Args:
            pos: the atomic number of the element

        Returns:
            the scattering factor of the element
        """
        els = []
        for el in self.sf:
            els.append(el[pos])
        return els

    # TODO: add docstrings for miscellaneous functions
    def all_z(self):
        return self.get_all(0)

    def all_short_names(self):
        return self.get_all(1)

    def all_long_names(self):
        return self.get_all(2)

    def all_valences(self):
        return self.get_all(3)

    def all_valence_electrons(self):
        return self.get_all(4)

    def all_covalent_radii(self):
        return self.get_all(5)

    def all_vdw_radii(self):
        return self.get_all(6)

    def all_metallic_radii(self):
        return self.get_all(7)

    def get_sf(self):
        return self.get_sf()

    def number_from_specie(specie):
        if type(specie) == int or type(specie) == float:
            if specie <= 105 and specie >= 1:
                index = int(specie)
            else:
                print(specie)
                print("Error: Atomic number must be between 1 and 105.")
                return
        elif type(specie) == str:
            try:
                el = Element(specie)
                index = el.z
            except:
                print("Error: Invalid atomic symbol, name, or number.")
                return
        elif type(specie) == Element:
            try:
                index = specie.z
            except:
                print("Error: Element object has no atomic number 'z'.")
                return
        else:
            try:
                el = Element(specie.number)
                index = el.z
            except:
                print("Error: Invalid atomic symbol, name, or number.")
                return
        return index
