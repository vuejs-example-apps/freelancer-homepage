# for an unknown (yet) reason, npm run build doesn't work now. so use this build.sh.

node_modules/cross-env/bin/cross-env.js NODE_ENV=production node_modules/webpack/bin/webpack.js --config build/webpack.client.config.js --progress --hide-modules

node_modules/cross-env/bin/cross-env.js NODE_ENV=production node_modules/webpack/bin/webpack.js --config build/webpack.server.config.js --progress --hide-modules
