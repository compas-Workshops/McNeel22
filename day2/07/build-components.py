import os
import tempfile


def build_ghuser_components(gh_io_folder=None, ironpython=None):
    """Builds Grasshopper components using GH Componentizer."""
    source_dir = os.path.abspath(".\components")
    target_dir = os.path.abspath(".\ghuser")
    repo_url = "https://github.com/compas-dev/compas-actions.ghpython_components.git"

    with tempfile.TemporaryDirectory("actions.ghcomponentizer") as action_dir:
        os.system("git clone {} {}".format(repo_url, action_dir))

        if not gh_io_folder:
            gh_io_folder = tempfile.mkdtemp("ghio")
            import compas_ghpython

            compas_ghpython.fetch_ghio_lib(gh_io_folder)

        if not ironpython:
            ironpython = "ipy"

        gh_io_folder = os.path.abspath(gh_io_folder)
        componentizer_script = os.path.join(action_dir, "componentize.py")

        cmd = "{} {} {} {}".format(ironpython, componentizer_script, source_dir, target_dir)
        cmd += ' --ghio "{}"'.format(gh_io_folder)
        os.system(cmd)


if __name__ == "__main__":
    build_ghuser_components()
