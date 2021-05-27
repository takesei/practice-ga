const docsDirList = require('./website.config.json').target.docs;
const fs = require('fs');

const getSameLayerFiles = path => {
  return fs.readdirSync(path, {withFileTypes: true })
    .flatMap(d => d.isFile() ? `${path}/${d.name}` : null)
    .filter(v => /.mdx?/.test(v))
    .map(v => v.split('.')[0])
    .filter(v => v !== null);
}

const getSameLayerDirs = path => {
  return fs.readdirSync(path, {withFileTypes: true })
    .flatMap(d => d.isFile() ? null: d.name)
    .filter(v => v !== null);
}

const genNest = (dir) => {
  const sameLayerDirs = getSameLayerDirs(dir);

  if (sameLayerDirs.length === 0) {
    return getSameLayerFiles(dir);
  }

  return sameLayerDirs.map(v => {
    const netedFiles = getSameLayerFiles(`${dir}/${v}`);

    if (netedFiles.length === 0) {
      return null;
    }

    return [
      ...getSameLayerFiles(`${dir}/${v}`), {
        type: 'category',
        label: v,
        items: genNest(`${dir}/${v}`),
      }
    ]

  }).filter(v => {
    return v !== null;
  }).filter(v => {
    const itemLen = v[v.length - 1].items.length;
    return itemLen !== 0;
  });

}

const side = docsDirList.map(dir => ({
  [dir]: genNest(`docs/${dir}`),
}));

console.log(side);

module.exports = {
  ...side,
};
