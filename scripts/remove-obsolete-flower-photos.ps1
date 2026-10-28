# Removes ONLY known obsolete photo crops from the previous flower patch.
# Run from the Astro project root after backing up the folder and copying the new patch.
$ErrorActionPreference = "Stop"
$paths = @(
    "public/images/tutorials/sunflower-flower-pen/textured-flower-center.webp"
    "public/images/tutorials/sunflower-flower-pen/crochet-pot.webp"
    "public/images/tutorials/sunflower-flower-pen/soil-insert.webp"
    "public/images/tutorials/sunflower-flower-pen/attach-flower-back.webp"
    "public/images/tutorials/sunflower-flower-pen/leaf-shape.webp"
    "public/images/tutorials/rose-flower-pen/rose-petal.webp"
    "public/images/tutorials/rose-flower-pen/layered-rose.webp"
    "public/images/tutorials/rose-flower-pen/rose-calyx.webp"
    "public/images/tutorials/rose-flower-pen/crochet-pot.webp"
    "public/images/tutorials/rose-flower-pen/soil-insert.webp"
    "public/images/tutorials/crocus-flower-pen/purple-petal.webp"
    "public/images/tutorials/crocus-flower-pen/nested-crocus-petals.webp"
    "public/images/tutorials/crocus-flower-pen/crochet-pot.webp"
    "public/images/tutorials/crocus-flower-pen/soil-insert.webp"
    "public/images/tutorials/hibiscus-flower-pen/shape-hibiscus.webp"
    "public/images/tutorials/hibiscus-flower-pen/hibiscus-petals.webp"
    "public/images/tutorials/hibiscus-flower-pen/crochet-pot.webp"
    "public/images/tutorials/hibiscus-flower-pen/soil-insert.webp"
    "public/images/tutorials/hibiscus-flower-pen/attach-stamen.webp"
)
foreach ($p in $paths) {
  if (Test-Path -LiteralPath $p -PathType Leaf) {
    Remove-Item -LiteralPath $p -Force
    Write-Host "Removed obsolete photo: $p"
  }
}
Write-Host "Cleanup complete. No pattern pages or folders were deleted."
