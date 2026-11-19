# Website pack
Prepares a downloadable file for users to upload to their websites.

- Make a new folder for this
  product under `workspace/product-shots/web/`. For each photo save a 2048 px
  square JPEG padded with white, a 1200 px WebP and a 600 px thumbnail. Give
  "Add a lifestyle shot" and "Make a homepage banner" options.
- A lifestyle shot is the Lifestyle style from [Touch-ups](photo-touch-ups.md),
  made and checked the same way. If the chosen photo is already Lifestyle, use it.
- A banner has the item in the right third, plain background on the left and no
  text, at 1920×1080 and 1920×640. For each size, place the chosen photo in the
  right third of a canvas that size, scaled to fit without cropping. Then use
  `media.generate_image` on the canvas, asking in the prompt text for a 16:9
  image for 1920×1080 or 3:1 for 1920×640, to fill the empty area by continuing
  the photo's own background, keeping the photo area unchanged. Fit the result
  to the canvas size without stretching. Check it by the Touch-ups rules, and that no seam
  shows around the photo and no text appears. If neither size passes, say so in
  one line and offer to try again.
- Add `product.txt`
  with the captions, alt text that describes only what is visible, and headline
  ideas from the user's facts. Then zip only this folder and link the zip and
  images with `sandbox://`. After adding a lifestyle shot or banner, zip the
  folder to a new file name and link that zip.
