# RayTracing

This repository contains a set of simple MATLAB scripts used to model
basic optical ray paths with lenses and mirrors. It was originally
created for Boun Photonics Lab and demonstrates how an object is
imaged through a sequence of optical components.

## Contents

- `RayTracing.m` – example script that sets up a small optical system
  using the functions listed below.
- `lens.m` – computes the imaging properties of a thin lens and can
  optionally draw the lens and ray lines.
- `mirror.m` – models reflection from a spherical mirror.
- `obj.m` – draws a simple object at a given location.
- `imagePlane.m` – helper used to draw the resulting image plane.

## Running the example

1. Open MATLAB (or an Octave environment).
2. Ensure all `.m` files are on the MATLAB path.
3. Run the script `RayTracing.m`.

The script will open a new figure and plot the object, lens, mirror,
and final image plane. You can edit the parameters inside
`RayTracing.m` to experiment with different object positions or focal
lengths.

## Notes

These scripts were written as a minimal demonstration and do not
include extensive error checking. They are intended for educational
purposes and may need adaptation for use in more complicated optical
systems.
