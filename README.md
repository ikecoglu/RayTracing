# RayTracing

This repository demonstrates a simple ray tracing setup originally developed for the Boun Photonics Lab.

The project now provides a Python implementation of the optical system. The earlier MATLAB scripts have been removed.

## Python usage

The repository includes the following modules:

- `ray_tracing.py` – example script that builds a small optical system.
- `lens.py` – computes the imaging properties of a thin lens.
- `mirror.py` – models reflection from a spherical mirror.
- `plane_mirror.py` – reflects rays from a flat mirror.
- `aperture.py` – draws an aperture used to limit the beam height.
- `obj.py` – draws a simple object at a given location.
- `image_plane.py` – helper used to draw the resulting image plane.

Install the required libraries and run the example:

```bash
pip install -r requirements.txt
python ray_tracing.py
```

The script will open a figure showing the object, lenses, mirror, aperture and plane mirror along with the final image plane. You can edit the parameters inside `ray_tracing.py` to experiment with different object positions or focal lengths.
