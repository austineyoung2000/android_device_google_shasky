# Android device tree for Google Pixel 8 family (shasky)

Unified LineageOS device repository for:

- `akita` — Pixel 8a
- `shiba` — Pixel 8
- `husky` — Pixel 8 Pro

Place this repository at `device/google/shasky`.

This tree was fused from the official LineageOS `android_device_google_akita`
and `android_device_google_shusky` repositories on the `lineage-24.0` branch.

## How the trees were fused

The existing Shusky layout was used as the base because it already supports
both Husky and Shiba. Akita was then added as the third product without making
its hardware configuration inherit Husky/Shiba-specific settings.

The fusion includes the following changes:

- Added the complete `akita/` device directory alongside `husky/` and `shiba/`.
- Added `aosp_akita.mk`, `device-akita.mk`, and `lineage_akita.mk`.
- Registered all six AOSP and LineageOS products in `AndroidProducts.mk`.
- Changed device-tree references from `device/google/akita` and
  `device/google/shusky` to the unified path `device/google/shasky`.
- Merged Akita's non-conflicting overlays, VINTF configuration, and product
  configuration into the shared repository.
- Kept Akita's board-info, recovery module lists, recovery init script,
  SELinux policy, and Wi-Fi configuration in Akita-specific paths. These files
  differ materially from Husky/Shiba and must not be flattened together.
- Retained Shusky's common configuration for Husky and Shiba, including their
  shared `BoardConfigCommon.mk` behavior.
- Combined `lineage.dependencies` while retaining the separate upstream
  `android_device_google_akita-kernels` and
  `android_device_google_shusky-kernels` repositories. The device trees are
  fused, but their kernel packages are intentionally not renamed or combined.
- Replaced the single-device root helper scripts with dispatchers that invoke
  the correct Akita, Husky, or Shiba extraction/setup script.
- Unified the root Soong namespace and license definition under the Shasky
  repository name.

This is a repository-level consolidation. It does not force Akita to inherit
Husky/Shiba display, modem, touch, recovery, Wi-Fi, or SELinux behavior.

## Repository dependencies

- `device/google/zuma`
- `device/google/akita-kernels`
- `device/google/shusky-kernels`

## Proprietary file helpers

```bash
./extract-files.py akita
./extract-files.py shiba
./extract-files.py husky

./setup-makefiles.py akita
./setup-makefiles.py shiba
./setup-makefiles.py husky
```

## Source snapshots

- Shusky: `6382d480f69b8ed55e75dd31c094e4bc04795e89`
- Akita: `858f7569eeca987d2c577ceb6a1a8cc78fdc377a`

Both snapshots were taken from their official LineageOS `lineage-24.0`
branches before the fusion.
