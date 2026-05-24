from pathlib import Path
import SimpleITK as sitk


def read_image(path: str):
    return sitk.ReadImage(str(path))


def resample_image(image, spacing=(2.0, 2.0, 2.0), interpolator=sitk.sitkLinear):
    original_spacing = image.GetSpacing()
    original_size = image.GetSize()

    new_size = [
        int(round(original_size[i] * (original_spacing[i] / spacing[i])))
        for i in range(3)
    ]

    resampler = sitk.ResampleImageFilter()
    resampler.SetOutputSpacing(spacing)
    resampler.SetSize(new_size)
    resampler.SetOutputDirection(image.GetDirection())
    resampler.SetOutputOrigin(image.GetOrigin())
    resampler.SetInterpolator(interpolator)

    return resampler.Execute(image)


def write_image(image, output_path: str):
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    sitk.WriteImage(image, str(output))


if __name__ == '__main__':
    print('Preprocessing module loaded.')
