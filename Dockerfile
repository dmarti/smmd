FROM ruby:2.6
RUN gem install jekyll bundler
WORKDIR /jekyll-site
ENTRYPOINT bundle update && bundle exec jekyll serve --incremental --host 0.0.0.0
