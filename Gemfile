source "https://rubygems.org"

# Mirrors what GitHub Pages runs server-side, so a local preview cannot pass
# while the deployed build fails. Pages builds this repo itself — no Action
# publishes it — so this Gemfile exists only for `bundle exec jekyll serve`.
gem "github-pages", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
end

gem "webrick"   # Ruby 3.x no longer bundles it
