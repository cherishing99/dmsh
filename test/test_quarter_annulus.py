import numpy as np
from helpers import assert_norm_equality

import dmsh


def test_quarter_annulus():
    h = 0.05
    disk0 = dmsh.Circle([0.0, 0.0], 0.25)
    disk1 = dmsh.Circle([0.0, 0.0], 1.0)
    diff0 = dmsh.Difference(disk1, disk0)

    rect = dmsh.Rectangle(0.0, 1.0, 0.0, 1.0)
    quarter = dmsh.Intersection([diff0, rect])

    points, cells = dmsh.generate(
        quarter,
        edge_size=lambda x: h + 0.1 * np.abs(disk0.dist(x)),
        tol=1.0e-10,
        max_steps=100,
    )

    ref_norms = [8.0232179592990462e01, 6.6832464479565372e00, 1.0000000000000000e00]
    assert_norm_equality(points.flatten(), ref_norms, 1.0e-10)
    return points, cells


if __name__ == "__main__":
    import meshio

    points, cells = test_quarter_annulus()
    meshio.Mesh(points, {"triangle": cells}).write("out.vtk")
