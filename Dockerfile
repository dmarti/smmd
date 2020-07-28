FROM ruby:2.6
RUN gem install jekyll bundler
WORKDIR /jekyll-site
ENTRYPOINT bundle install && bundle exec jekyll serve --profile --livereload --incremental --strict-front-matter --host 0.0.0.0
