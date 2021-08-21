FROM ruby:2.6
WORKDIR /jekyll-site
RUN gem install jekyll bundler
ENTRYPOINT bundle install && bundle update github-pages && bundle exec jekyll serve --profile --livereload --incremental --strict-front-matter --host 0.0.0.0
