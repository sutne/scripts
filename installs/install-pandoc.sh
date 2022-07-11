# Start by installing basictex
brew --cask install basictex

# Install all packages used by my templates, not contained in basictex
optional_packages="lastpage enumitem"
for package in $optional_packages; do
    sudo tlmgr install $package
done

# Install pandoc
brew install pandoc
brew install pandoc-crossref
