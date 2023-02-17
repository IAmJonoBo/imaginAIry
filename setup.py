import sys

from setuptools import find_packages, setup

is_for_windows = len(sys.argv) >= 3 and sys.argv[2].startswith("--plat-name=win")

if is_for_windows:
    scripts = None
    entry_points = {
        "console_scripts": [
            "imagine=imaginairy.cmds:imagine_cmd",
            "aimg=imaginairy.cmds:aimg",
        ],
    }
else:
    scripts = ["imaginairy/bin/aimg", "imaginairy/bin/imagine"]
    entry_points = None


with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="imaginAIry",
    author="Bryce Drennan",
    # author_email="b r y p y d o t io",
    version="10.0.0",
    description="AI imagined images. Pythonic generation of stable diffusion images.",
    long_description=readme,
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://github.com/brycedrennan/imaginAIry/blob/master/README.md",
        "Source": "https://github.com/brycedrennan/imaginAIry",
    },
    packages=find_packages(include=("imaginairy", "imaginairy.*")),
    scripts=scripts,
    entry_points=entry_points,
    package_data={
        "imaginairy": [
            "configs/*.yaml",
            "data/*.*",
            "bin/*.*",
            "enhancers/phraselists/*.txt",
            "vendored/clip/*.txt.gz",
            "vendored/clipseg/*.pth",
            "vendored/blip/configs/*.*",
            "vendored/noodle_soup_prompts/*.*",
            "vendored/noodle_soup_prompts/LICENSE",
        ]
    },
    install_requires=[
        "click",
        "click-help-colors",
        "click-shell",
        "protobuf != 3.20.2, != 3.19.5",
        "facexlib",
        "fairscale>=0.4.4",  # for vendored blip
        "ftfy",  # for vendored clip
        "torch>=1.2.0",
        "numpy",
        "tqdm",
        "diffusers",
        "imageio>=2.9.0",
        "Pillow>=8.0.0",
        "psutil",
        "pytorch-lightning>=1.4.2",
        "omegaconf>=2.1.1",
        "open-clip-torch",
        "opencv-python",
        "requests",
        "einops>=0.3.0",
        "safetensors",
        "timm>=0.4.12",  # for vendored blip
        "torchdiffeq",
        "transformers>=4.19.2",
        "torchmetrics>=0.6.0",
        "torchvision>=0.13.1",
        "kornia>=0.6",
        "xformers>=0.0.16; sys_platform!='darwin'",
    ],
)
