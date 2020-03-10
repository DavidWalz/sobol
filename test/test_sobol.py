import numpy as np
import io
import sobol

samples_sobol_3_5 = np.genfromtxt(
    io.StringIO(
        """# sobol_seq.i4_sobol_generate(3, 5)
0.5,0.5,0.5
0.75,0.25,0.75
0.25,0.75,0.25
0.375,0.375,0.625
0.875,0.875,0.125
"""
    ),
    delimiter=",",
)

samples_sobol_40_50 = np.genfromtxt(
    io.StringIO(
        """# sobol_seq.i4_sobol_generate(40, 50)
0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5
0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25
0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75
0.375,0.375,0.625,0.125,0.875,0.875,0.125,0.625,0.125,0.875,0.375,0.625,0.125,0.375,0.625,0.125,0.625,0.375,0.375,0.875,0.875,0.625,0.125,0.875,0.125,0.875,0.875,0.125,0.625,0.625,0.375,0.375,0.375,0.375,0.625,0.125,0.875,0.875,0.125,0.625
0.875,0.875,0.125,0.625,0.375,0.375,0.625,0.125,0.625,0.375,0.875,0.125,0.625,0.875,0.125,0.625,0.125,0.875,0.875,0.375,0.375,0.125,0.625,0.375,0.625,0.375,0.375,0.625,0.125,0.125,0.875,0.875,0.875,0.875,0.125,0.625,0.375,0.375,0.625,0.125
0.625,0.125,0.375,0.375,0.125,0.625,0.875,0.875,0.375,0.125,0.125,0.375,0.375,0.625,0.875,0.875,0.375,0.125,0.625,0.625,0.125,0.875,0.875,0.625,0.375,0.125,0.625,0.875,0.875,0.375,0.125,0.625,0.625,0.125,0.375,0.375,0.125,0.625,0.875,0.875
0.125,0.625,0.875,0.875,0.625,0.125,0.375,0.375,0.875,0.625,0.625,0.875,0.875,0.125,0.375,0.375,0.875,0.625,0.125,0.125,0.625,0.375,0.375,0.125,0.875,0.625,0.125,0.375,0.375,0.875,0.625,0.125,0.125,0.625,0.875,0.875,0.625,0.125,0.375,0.375
0.1875,0.3125,0.3125,0.6875,0.5625,0.1875,0.0625,0.9375,0.1875,0.0625,0.6875,0.8125,0.5625,0.6875,0.1875,0.6875,0.1875,0.0625,0.0625,0.8125,0.9375,0.3125,0.5625,0.3125,0.4375,0.4375,0.6875,0.4375,0.8125,0.5625,0.9375,0.8125,0.1875,0.3125,0.3125,0.6875,0.5625,0.1875,0.0625,0.9375
0.6875,0.8125,0.8125,0.1875,0.0625,0.6875,0.5625,0.4375,0.6875,0.5625,0.1875,0.3125,0.0625,0.1875,0.6875,0.1875,0.6875,0.5625,0.5625,0.3125,0.4375,0.8125,0.0625,0.8125,0.9375,0.9375,0.1875,0.9375,0.3125,0.0625,0.4375,0.3125,0.6875,0.8125,0.8125,0.1875,0.0625,0.6875,0.5625,0.4375
0.9375,0.0625,0.5625,0.9375,0.3125,0.4375,0.8125,0.6875,0.4375,0.8125,0.9375,0.0625,0.8125,0.4375,0.4375,0.4375,0.9375,0.3125,0.8125,0.5625,0.1875,0.0625,0.3125,0.0625,0.1875,0.6875,0.9375,0.6875,0.5625,0.3125,0.6875,0.0625,0.9375,0.0625,0.5625,0.9375,0.3125,0.4375,0.8125,0.6875
0.4375,0.5625,0.0625,0.4375,0.8125,0.9375,0.3125,0.1875,0.9375,0.3125,0.4375,0.5625,0.3125,0.9375,0.9375,0.9375,0.4375,0.8125,0.3125,0.0625,0.6875,0.5625,0.8125,0.5625,0.6875,0.1875,0.4375,0.1875,0.0625,0.8125,0.1875,0.5625,0.4375,0.5625,0.0625,0.4375,0.8125,0.9375,0.3125,0.1875
0.3125,0.1875,0.9375,0.5625,0.4375,0.8125,0.1875,0.3125,0.0625,0.9375,0.8125,0.4375,0.6875,0.8125,0.5625,0.5625,0.5625,0.4375,0.4375,0.1875,0.0625,0.9375,0.6875,0.6875,0.3125,0.5625,0.3125,0.3125,0.4375,0.1875,0.5625,0.6875,0.3125,0.1875,0.9375,0.5625,0.4375,0.8125,0.1875,0.3125
0.8125,0.6875,0.4375,0.0625,0.9375,0.3125,0.6875,0.8125,0.5625,0.4375,0.3125,0.9375,0.1875,0.3125,0.0625,0.0625,0.0625,0.9375,0.9375,0.6875,0.5625,0.4375,0.1875,0.1875,0.8125,0.0625,0.8125,0.8125,0.9375,0.6875,0.0625,0.1875,0.8125,0.6875,0.4375,0.0625,0.9375,0.3125,0.6875,0.8125
0.5625,0.4375,0.1875,0.8125,0.6875,0.5625,0.9375,0.0625,0.3125,0.1875,0.5625,0.6875,0.9375,0.0625,0.8125,0.3125,0.3125,0.1875,0.6875,0.4375,0.8125,0.6875,0.4375,0.9375,0.0625,0.3125,0.0625,0.5625,0.1875,0.9375,0.8125,0.4375,0.5625,0.4375,0.1875,0.8125,0.6875,0.5625,0.9375,0.0625
0.0625,0.9375,0.6875,0.3125,0.1875,0.0625,0.4375,0.5625,0.8125,0.6875,0.0625,0.1875,0.4375,0.5625,0.3125,0.8125,0.8125,0.6875,0.1875,0.9375,0.3125,0.1875,0.9375,0.4375,0.5625,0.8125,0.5625,0.0625,0.6875,0.4375,0.3125,0.9375,0.0625,0.9375,0.6875,0.3125,0.1875,0.0625,0.4375,0.5625
0.09375,0.46875,0.84375,0.40625,0.28125,0.34375,0.53125,0.84375,0.78125,0.40625,0.40625,0.84375,0.84375,0.15625,0.78125,0.53125,0.09375,0.53125,0.34375,0.46875,0.34375,0.96875,0.09375,0.40625,0.40625,0.53125,0.71875,0.65625,0.40625,0.90625,0.96875,0.84375,0.09375,0.46875,0.84375,0.40625,0.28125,0.34375,0.53125,0.84375
0.59375,0.96875,0.34375,0.90625,0.78125,0.84375,0.03125,0.34375,0.28125,0.90625,0.90625,0.34375,0.34375,0.65625,0.28125,0.03125,0.59375,0.03125,0.84375,0.96875,0.84375,0.46875,0.59375,0.90625,0.90625,0.03125,0.21875,0.15625,0.90625,0.40625,0.46875,0.34375,0.59375,0.96875,0.34375,0.90625,0.78125,0.84375,0.03125,0.34375
0.84375,0.21875,0.09375,0.15625,0.53125,0.09375,0.28125,0.59375,0.53125,0.65625,0.15625,0.09375,0.59375,0.90625,0.53125,0.28125,0.84375,0.78125,0.59375,0.21875,0.59375,0.71875,0.84375,0.15625,0.15625,0.28125,0.96875,0.40625,0.15625,0.15625,0.71875,0.09375,0.84375,0.21875,0.09375,0.15625,0.53125,0.09375,0.28125,0.59375
0.34375,0.71875,0.59375,0.65625,0.03125,0.59375,0.78125,0.09375,0.03125,0.15625,0.65625,0.59375,0.09375,0.40625,0.03125,0.78125,0.34375,0.28125,0.09375,0.71875,0.09375,0.21875,0.34375,0.65625,0.65625,0.78125,0.46875,0.90625,0.65625,0.65625,0.21875,0.59375,0.34375,0.71875,0.59375,0.65625,0.03125,0.59375,0.78125,0.09375
0.46875,0.09375,0.46875,0.28125,0.65625,0.71875,0.65625,0.46875,0.90625,0.53125,0.03125,0.46875,0.96875,0.28125,0.40625,0.65625,0.71875,0.90625,0.21875,0.59375,0.71875,0.34375,0.21875,0.53125,0.28125,0.40625,0.34375,0.53125,0.78125,0.28125,0.59375,0.71875,0.46875,0.09375,0.46875,0.28125,0.65625,0.71875,0.65625,0.46875
0.96875,0.59375,0.96875,0.78125,0.15625,0.21875,0.15625,0.96875,0.40625,0.03125,0.53125,0.96875,0.46875,0.78125,0.90625,0.15625,0.21875,0.40625,0.71875,0.09375,0.21875,0.84375,0.71875,0.03125,0.78125,0.90625,0.84375,0.03125,0.28125,0.78125,0.09375,0.21875,0.96875,0.59375,0.96875,0.78125,0.15625,0.21875,0.15625,0.96875
0.71875,0.34375,0.71875,0.03125,0.40625,0.96875,0.40625,0.21875,0.65625,0.28125,0.28125,0.71875,0.71875,0.53125,0.15625,0.40625,0.46875,0.65625,0.96875,0.84375,0.46875,0.09375,0.96875,0.78125,0.03125,0.65625,0.09375,0.28125,0.53125,0.53125,0.84375,0.46875,0.71875,0.34375,0.71875,0.03125,0.40625,0.96875,0.40625,0.21875
0.21875,0.84375,0.21875,0.53125,0.90625,0.46875,0.90625,0.71875,0.15625,0.78125,0.78125,0.21875,0.21875,0.03125,0.65625,0.90625,0.96875,0.15625,0.46875,0.34375,0.96875,0.59375,0.46875,0.28125,0.53125,0.15625,0.59375,0.78125,0.03125,0.03125,0.34375,0.96875,0.21875,0.84375,0.21875,0.53125,0.90625,0.46875,0.90625,0.71875
0.15625,0.15625,0.53125,0.84375,0.84375,0.40625,0.59375,0.15625,0.96875,0.46875,0.84375,0.03125,0.28125,0.59375,0.96875,0.21875,0.15625,0.59375,0.28125,0.65625,0.65625,0.65625,0.53125,0.21875,0.09375,0.96875,0.03125,0.84375,0.71875,0.46875,0.03125,0.03125,0.15625,0.15625,0.53125,0.84375,0.84375,0.40625,0.59375,0.15625
0.65625,0.65625,0.03125,0.34375,0.34375,0.90625,0.09375,0.65625,0.46875,0.96875,0.34375,0.53125,0.78125,0.09375,0.46875,0.71875,0.65625,0.09375,0.78125,0.15625,0.15625,0.15625,0.03125,0.71875,0.59375,0.46875,0.53125,0.34375,0.21875,0.96875,0.53125,0.53125,0.65625,0.65625,0.03125,0.34375,0.34375,0.90625,0.09375,0.65625
0.90625,0.40625,0.28125,0.59375,0.09375,0.15625,0.34375,0.40625,0.71875,0.71875,0.59375,0.78125,0.03125,0.34375,0.71875,0.96875,0.90625,0.84375,0.53125,0.90625,0.40625,0.90625,0.28125,0.46875,0.34375,0.21875,0.28125,0.09375,0.96875,0.71875,0.28125,0.78125,0.90625,0.40625,0.28125,0.59375,0.09375,0.15625,0.34375,0.40625
0.40625,0.90625,0.78125,0.09375,0.59375,0.65625,0.84375,0.90625,0.21875,0.21875,0.09375,0.28125,0.53125,0.84375,0.21875,0.46875,0.40625,0.34375,0.03125,0.40625,0.90625,0.40625,0.78125,0.96875,0.84375,0.71875,0.78125,0.59375,0.46875,0.21875,0.78125,0.28125,0.40625,0.90625,0.78125,0.09375,0.59375,0.65625,0.84375,0.90625
0.28125,0.28125,0.15625,0.96875,0.21875,0.53125,0.71875,0.53125,0.84375,0.59375,0.71875,0.65625,0.40625,0.96875,0.34375,0.09375,0.53125,0.96875,0.15625,0.28125,0.28125,0.03125,0.65625,0.84375,0.21875,0.09375,0.90625,0.96875,0.09375,0.84375,0.40625,0.40625,0.28125,0.28125,0.15625,0.96875,0.21875,0.53125,0.71875,0.53125
0.78125,0.78125,0.65625,0.46875,0.71875,0.03125,0.21875,0.03125,0.34375,0.09375,0.21875,0.15625,0.90625,0.46875,0.84375,0.59375,0.03125,0.46875,0.65625,0.78125,0.78125,0.53125,0.15625,0.34375,0.71875,0.59375,0.40625,0.46875,0.59375,0.34375,0.90625,0.90625,0.78125,0.78125,0.65625,0.46875,0.71875,0.03125,0.21875,0.03125
0.53125,0.03125,0.90625,0.71875,0.96875,0.78125,0.46875,0.78125,0.59375,0.34375,0.96875,0.40625,0.15625,0.21875,0.09375,0.84375,0.28125,0.71875,0.90625,0.03125,0.53125,0.28125,0.40625,0.59375,0.46875,0.84375,0.65625,0.21875,0.34375,0.09375,0.15625,0.65625,0.53125,0.03125,0.90625,0.71875,0.96875,0.78125,0.46875,0.78125
0.03125,0.53125,0.40625,0.21875,0.46875,0.28125,0.96875,0.28125,0.09375,0.84375,0.46875,0.90625,0.65625,0.71875,0.59375,0.34375,0.78125,0.21875,0.40625,0.53125,0.03125,0.78125,0.90625,0.09375,0.96875,0.34375,0.15625,0.71875,0.84375,0.59375,0.65625,0.15625,0.03125,0.53125,0.40625,0.21875,0.46875,0.28125,0.96875,0.28125
0.046875,0.265625,0.609375,0.578125,0.703125,0.640625,0.265625,0.671875,0.578125,0.046875,0.203125,0.140625,0.359375,0.171875,0.109375,0.265625,0.859375,0.078125,0.953125,0.453125,0.390625,0.546875,0.828125,0.265625,0.546875,0.328125,0.484375,0.546875,0.640625,0.984375,0.546875,0.921875,0.546875,0.765625,0.109375,0.078125,0.203125,0.140625,0.765625,0.171875
0.546875,0.765625,0.109375,0.078125,0.203125,0.140625,0.765625,0.171875,0.078125,0.546875,0.703125,0.640625,0.859375,0.671875,0.609375,0.765625,0.359375,0.578125,0.453125,0.953125,0.890625,0.046875,0.328125,0.765625,0.046875,0.828125,0.984375,0.046875,0.140625,0.484375,0.046875,0.421875,0.046875,0.265625,0.609375,0.578125,0.703125,0.640625,0.265625,0.671875
0.796875,0.015625,0.359375,0.828125,0.453125,0.890625,0.515625,0.921875,0.828125,0.796875,0.453125,0.890625,0.109375,0.921875,0.359375,0.515625,0.109375,0.328125,0.203125,0.203125,0.640625,0.796875,0.078125,0.015625,0.796875,0.578125,0.234375,0.296875,0.890625,0.234375,0.796875,0.171875,0.296875,0.515625,0.859375,0.328125,0.953125,0.390625,0.015625,0.421875
0.296875,0.515625,0.859375,0.328125,0.953125,0.390625,0.015625,0.421875,0.328125,0.296875,0.953125,0.390625,0.609375,0.421875,0.859375,0.015625,0.609375,0.828125,0.703125,0.703125,0.140625,0.296875,0.578125,0.515625,0.296875,0.078125,0.734375,0.796875,0.390625,0.734375,0.296875,0.671875,0.796875,0.015625,0.359375,0.828125,0.453125,0.890625,0.515625,0.921875
0.421875,0.140625,0.234375,0.703125,0.328125,0.265625,0.390625,0.046875,0.703125,0.921875,0.328125,0.515625,0.484375,0.296875,0.734375,0.390625,0.484375,0.453125,0.578125,0.578125,0.515625,0.171875,0.953125,0.640625,0.671875,0.703125,0.609375,0.671875,0.015625,0.359375,0.921875,0.546875,0.921875,0.640625,0.734375,0.203125,0.828125,0.765625,0.890625,0.546875
0.921875,0.640625,0.734375,0.203125,0.828125,0.765625,0.890625,0.546875,0.203125,0.421875,0.828125,0.015625,0.984375,0.796875,0.234375,0.890625,0.984375,0.953125,0.078125,0.078125,0.015625,0.671875,0.453125,0.140625,0.171875,0.203125,0.109375,0.171875,0.515625,0.859375,0.421875,0.046875,0.421875,0.140625,0.234375,0.703125,0.328125,0.265625,0.390625,0.046875
0.671875,0.390625,0.984375,0.953125,0.578125,0.015625,0.640625,0.296875,0.953125,0.171875,0.078125,0.265625,0.234375,0.546875,0.984375,0.640625,0.734375,0.203125,0.328125,0.828125,0.265625,0.421875,0.203125,0.890625,0.921875,0.453125,0.859375,0.421875,0.265625,0.609375,0.671875,0.296875,0.171875,0.890625,0.484375,0.453125,0.078125,0.515625,0.140625,0.796875
0.171875,0.890625,0.484375,0.453125,0.078125,0.515625,0.140625,0.796875,0.453125,0.671875,0.578125,0.765625,0.734375,0.046875,0.484375,0.140625,0.234375,0.703125,0.828125,0.328125,0.765625,0.921875,0.703125,0.390625,0.421875,0.953125,0.359375,0.921875,0.765625,0.109375,0.171875,0.796875,0.671875,0.390625,0.984375,0.953125,0.578125,0.015625,0.640625,0.296875
0.234375,0.078125,0.796875,0.140625,0.140625,0.578125,0.328125,0.359375,0.640625,0.109375,0.515625,0.953125,0.796875,0.609375,0.171875,0.953125,0.921875,0.015625,0.890625,0.640625,0.578125,0.859375,0.265625,0.078125,0.984375,0.140625,0.796875,0.984375,0.453125,0.421875,0.484375,0.234375,0.734375,0.578125,0.296875,0.640625,0.640625,0.078125,0.828125,0.859375
0.734375,0.578125,0.296875,0.640625,0.640625,0.078125,0.828125,0.859375,0.140625,0.609375,0.015625,0.453125,0.296875,0.109375,0.671875,0.453125,0.421875,0.515625,0.390625,0.140625,0.078125,0.359375,0.765625,0.578125,0.484375,0.640625,0.296875,0.484375,0.953125,0.921875,0.984375,0.734375,0.234375,0.078125,0.796875,0.140625,0.140625,0.578125,0.328125,0.359375
0.984375,0.328125,0.046875,0.390625,0.890625,0.828125,0.578125,0.109375,0.890625,0.859375,0.765625,0.203125,0.546875,0.359375,0.421875,0.203125,0.171875,0.265625,0.140625,0.890625,0.328125,0.609375,0.515625,0.328125,0.734375,0.890625,0.546875,0.234375,0.203125,0.671875,0.234375,0.984375,0.484375,0.828125,0.546875,0.890625,0.390625,0.328125,0.078125,0.609375
0.484375,0.828125,0.546875,0.890625,0.390625,0.328125,0.078125,0.609375,0.390625,0.359375,0.265625,0.703125,0.046875,0.859375,0.921875,0.703125,0.671875,0.765625,0.640625,0.390625,0.828125,0.109375,0.015625,0.828125,0.234375,0.390625,0.046875,0.734375,0.703125,0.171875,0.734375,0.484375,0.984375,0.328125,0.046875,0.390625,0.890625,0.828125,0.578125,0.109375
0.359375,0.453125,0.421875,0.015625,0.765625,0.453125,0.453125,0.984375,0.515625,0.984375,0.890625,0.328125,0.921875,0.984375,0.546875,0.828125,0.296875,0.390625,0.515625,0.265625,0.453125,0.484375,0.390625,0.953125,0.859375,0.765625,0.171875,0.859375,0.828125,0.796875,0.109375,0.359375,0.859375,0.953125,0.921875,0.515625,0.265625,0.953125,0.953125,0.484375
0.859375,0.953125,0.921875,0.515625,0.265625,0.953125,0.953125,0.484375,0.015625,0.484375,0.390625,0.828125,0.421875,0.484375,0.046875,0.328125,0.796875,0.890625,0.015625,0.765625,0.953125,0.984375,0.890625,0.453125,0.359375,0.265625,0.671875,0.359375,0.328125,0.296875,0.609375,0.859375,0.359375,0.453125,0.421875,0.015625,0.765625,0.453125,0.453125,0.984375
0.609375,0.203125,0.671875,0.265625,0.015625,0.203125,0.703125,0.734375,0.765625,0.234375,0.640625,0.578125,0.671875,0.234375,0.796875,0.078125,0.546875,0.140625,0.265625,0.015625,0.703125,0.234375,0.640625,0.703125,0.609375,0.015625,0.421875,0.109375,0.578125,0.046875,0.359375,0.609375,0.109375,0.703125,0.171875,0.765625,0.515625,0.703125,0.203125,0.234375
0.109375,0.703125,0.171875,0.765625,0.515625,0.703125,0.203125,0.234375,0.265625,0.734375,0.140625,0.078125,0.171875,0.734375,0.296875,0.578125,0.046875,0.640625,0.765625,0.515625,0.203125,0.734375,0.140625,0.203125,0.109375,0.515625,0.921875,0.609375,0.078125,0.546875,0.859375,0.109375,0.609375,0.203125,0.671875,0.265625,0.015625,0.203125,0.703125,0.734375
0.078125,0.234375,0.265625,0.984375,0.984375,0.984375,0.796875,0.453125,0.359375,0.390625,0.359375,0.984375,0.515625,0.015625,0.828125,0.796875,0.765625,0.609375,0.671875,0.046875,0.234375,0.453125,0.796875,0.171875,0.890625,0.859375,0.765625,0.140625,0.796875,0.078125,0.453125,0.203125,0.578125,0.734375,0.765625,0.484375,0.484375,0.484375,0.296875,0.953125
0.578125,0.734375,0.765625,0.484375,0.484375,0.484375,0.296875,0.953125,0.859375,0.890625,0.859375,0.484375,0.015625,0.515625,0.328125,0.296875,0.265625,0.109375,0.171875,0.546875,0.734375,0.953125,0.296875,0.671875,0.390625,0.359375,0.265625,0.640625,0.296875,0.578125,0.953125,0.703125,0.078125,0.234375,0.265625,0.984375,0.984375,0.984375,0.796875,0.453125
0.828125,0.484375,0.515625,0.734375,0.234375,0.734375,0.046875,0.203125,0.109375,0.640625,0.109375,0.234375,0.765625,0.765625,0.578125,0.046875,0.015625,0.859375,0.421875,0.296875,0.984375,0.203125,0.046875,0.421875,0.640625,0.109375,0.515625,0.890625,0.546875,0.828125,0.203125,0.953125,0.328125,0.984375,0.015625,0.234375,0.734375,0.234375,0.546875,0.703125
"""
    ),
    delimiter=",",
)


def test_bit_lo0():
    assert sobol.bit_lo0(0) == 0  # 0
    assert sobol.bit_lo0(1) == 1  # 1
    assert sobol.bit_lo0(2) == 0  # 10
    assert sobol.bit_lo0(3) == 2  # 11
    assert sobol.bit_lo0(4) == 0  # 100
    assert sobol.bit_lo0(5) == 1  # 101
    assert sobol.bit_lo0(6) == 0  # 110
    assert sobol.bit_lo0(7) == 3  # 111
    assert sobol.bit_lo0(8) == 0  # 1000
    assert sobol.bit_lo0(9) == 1  # 1001
    assert sobol.bit_lo0(10) == 0  # 1010
    assert sobol.bit_lo0(11) == 2  # 1011
    assert sobol.bit_lo0(12) == 0  # 1100
    assert sobol.bit_lo0(13) == 1  # 1101
    assert sobol.bit_lo0(14) == 0  # 1110
    assert sobol.bit_lo0(15) == 4  # 1111
    assert sobol.bit_lo0(16) == 0  # 10000
    assert sobol.bit_lo0(17) == 1  # 10001
    assert sobol.bit_lo0(1023) == 10  # 1111111111
    assert sobol.bit_lo0(1024) == 0  # 10000000000
    assert sobol.bit_lo0(1025) == 1  # 10000000001


def test_sample():
    assert np.allclose(samples_sobol_3_5, sobol.sample(3, 5),)
    assert np.allclose(samples_sobol_40_50, sobol.sample(40, 50),)
