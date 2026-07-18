#!/bin/bash
set -euo pipefail

# This website is built with Jekyll; use Ruby 3.3.x (Ruby >= 3.4 / 4.x breaks the stack).

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

needs_ruby33() {
  if ! command -v ruby >/dev/null 2>&1; then
    return 0
  fi
  # Exit 0 (true) when Ruby is outside the supported range: < 3.0 or >= 3.4
  ruby -e 'v = Gem::Version.new(RUBY_VERSION); exit(v < Gem::Version.new("3.0") || v >= Gem::Version.new("3.4") ? 0 : 1)'
}

if needs_ruby33; then
  echo "Unsupported Ruby ($(ruby -v 2>/dev/null || echo 'not found')); ensuring ruby@3.3 via Homebrew..."

  if ! command -v brew >/dev/null 2>&1; then
    echo "Error: Homebrew is required. Install from https://brew.sh" >&2
    exit 1
  fi

  # Remove the default Homebrew ruby formula if present (often 4.x)
  if brew list --formula ruby >/dev/null 2>&1; then
    brew uninstall ruby
  fi

  brew install ruby@3.3
  brew link ruby@3.3 --force --overwrite

  export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
fi

# Prefer ruby@3.3 when it is installed (even if another ruby is already acceptable)
if [[ -x "$(brew --prefix ruby@3.3 2>/dev/null)/bin/ruby" ]]; then
  export PATH="$(brew --prefix ruby@3.3)/bin:$PATH"
fi

echo "Using $(ruby -v) at $(which ruby)"

bundle config set --local path 'vendor/bundle'
bundle install
bundle exec jekyll serve -l -H localhost -p 4000
