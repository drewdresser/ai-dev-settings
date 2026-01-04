set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

default:
  @just --list

# Install into the current project repo (pwd)
install profile="ship":
  ./scripts/install_project.sh {{profile}} "{{justfile_directory()}}"

install-safe:
  just install safe

install-ship:
  just install ship

install-yolo:
  just install yolo

# Symlink global configs into your home directory
link-global:
  ./scripts/link_global.sh "{{justfile_directory()}}"

# Quick sanity check: show what would be installed
preview profile="ship":
  @echo "Profile: {{profile}}"
  @find "profiles/{{profile}}" -maxdepth 4 -type f -print

