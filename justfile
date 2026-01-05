set shell := ["bash", "-eu", "-o", "pipefail", "-c"]

default:
  @just --list

# Install into the current project repo (where you ran just from)
install:
  ./scripts/install_project.sh "{{justfile_directory()}}" "{{invocation_directory()}}"

# Symlink global configs into your home directory
link-global:
  ./scripts/link_global.sh "{{justfile_directory()}}"

# Quick sanity check: show what would be installed
preview:
  @echo "Files to install:"
  @find "project" -type f -print
