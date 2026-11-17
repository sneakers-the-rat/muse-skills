# Generate Meta ad media

This guide covers generating images and video for an accepted creative plan. Whether generation is available depends on what the ad is about.

## When generation isn't available

For ads about politics or social issues, housing, jobs, financial products, healthcare, medicines, education, alcohol or gambling, you can't use AI to make images or video, write ad text, or create new media from the advertiser's own photo. What's advertised decides this, as [safety](safety.md) explains.

- The advertiser's own images, videos and words still work. Their media can run as it is, with a note that Meta may crop or resize it, or use Meta's own enhancements through `advantage_plus_creative`. Trimming their words to fit or fixing a typo keeps them their words; writing a new headline doesn't.

- Political and social issue ads are stricter: no Meta enhancements either, and their media and words run exactly as given.

- Tell the advertiser that generated creative isn't available for this ad. That isn't Meta saying the ad is banned.

## Generate images and video

- Ad images come from `meta-ads-cli creative generate-image`, which makes each image at the exact shape for Feed, Stories or Reels and checks the result. Its flags are in `--help`.

- The prompt is the advertiser's request in their own words, with separate constraints as separate entries. A source image adapts one of the advertiser's images.

- Video comes from `media.generate_video` with the same request, saved to `workspace/your_files`. It doesn't set a shape, so the prompt states it, 9:16 for Stories and Reels or 4:5 for Feed, and the file is measured afterward. A video that doesn't fit sends the plan back for another look, not another try.

- A single video ad needs a thumbnail, taken as a still frame from that video.

- After the direction is accepted, a prompt can add small production detail that fits it. It doesn't change the subject, scene, style, source, shape, text in the image, message or limits; anything like that goes back to the plan. Text required in the image is quoted exactly.

- Each generated file keeps its local path, size and media handle for execution. Editing a file makes a new asset.

## What generated media can show

- Generated media and prompts shouldn't include real public figures or other companies' brands, logos or characters, even indirectly. A dealer's or reseller's marks should come only from the advertiser's own media. Editing a photo redraws all of it, so photos showing any of these should run as supplied. If you can't tell whose logo it is, ask the advertiser.

- Generated media shouldn't show restricted goods as its subject: tobacco and vapes, alcohol, cannabis and other drugs, weapons and gambling. When generation is available, the image can show the setting around them: the place, the people, the occasion or the packaging the advertiser supplies. Something that's only in the background isn't the subject.

- Each image is checked after it's generated, not only its prompt, for recognizable people, logos, wordmarks, characters and artwork.

- Seals, badges, ratings and numbers in an image are claims, as [safety](safety.md) explains. The generator redraws a real mark rather than copying it, so a real seal or award needs the advertiser's finished artwork. The plan says what the image claims before approval.

- Generated media keeps its AI label and isn't presented as a real person, place or product.
