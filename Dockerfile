FROM ruby:2.6
RUN gem install jekyll bundler
WORKDIR /jekyll-site
ENTRYPOINT bundle update && bundle exec jekyll serve --disable-disk-cache --verbose --profile --livereload --incremental --strict-front-matter --incremental --host 0.0.0.0
