from cookiecutter.main import cookiecutter
import pathlib

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_generated_files(tmpdir):
    generate(
        tmpdir,
        {
            "plugin_name": "vidtoolz-foo",
            "description": "blah",
        },
    )
    assert paths(tmpdir) == {'vidtoolz-foo/.github', 'vidtoolz-foo/.github/workflows/test.yml', 'vidtoolz-foo', 'vidtoolz-foo/LICENSE',
                             'vidtoolz-foo/README.md', 'vidtoolz-foo/tests', 'vidtoolz-foo/vidtoolz_foo',
                             'vidtoolz-foo/.github/workflows/publish.yml', 'vidtoolz-foo/.github/workflows',
                             'vidtoolz-foo/tests/test_vidtoolz_foo.py', 'vidtoolz-foo/vidtoolz_foo/__init__.py',
                             'vidtoolz-foo/pyproject.toml', 'vidtoolz-foo/.gitignore','vidtoolz-foo/.github/workflows'}

def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}
