/** @type {import('@docusaurus/types').DocusaurusConfig} */
const fs = require('fs');
const config = require('./website.config.json')

const getDocsDirs = () => {
  let docsDir = fs.readdirSync('./docs', { withFileTypes: true })
    .flatMap(d => d.isFile() ? null: d.name)
    .filter(v => v !== null);
  let diff = docsDir.filter(x => !config.target.docs.includes(x));
  return config.target.docs.concat(diff);
}


module.exports = {
  title: 'Sample Tech Stats Website',
  tagline: 'Dinosaurs are cool',
  url: 'https://takesei.github.io',
  baseUrl: '/tech-stats/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'takesei', // Usually your GitHub org/user name.
  projectName: 'tech-stats', // Usually your repo name.
  themeConfig: {
    prism: {
      theme: require('prism-react-renderer/themes/github'),
      darkTheme: require('prism-react-renderer/themes/dracula'),
      additionalLanguages: ['python', 'julia', 'r', 'markdown']
    },
    navbar: {
      title: 'Tech Stats',
      hideOnScroll: true,
      logo: {
        alt: 'Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        ...getDocsDirs().map(pj => ({
          type: 'doc',
          docId: `${pj}/intro`,
          position: 'left',
          label: `${pj}`,
        })),
        {
          href: 'https://github.com/takesei/tech-stats',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'About author',
          items: [
            {
              label: 'twitter',
              href: 'https://twitter.com/honyamorake',
            },
            {
              label: 'Github',
              href: 'https://github.com/takesei',
            },
          ],
        },
        {
          title: 'About Project',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/takesei/tech-stats',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Takesei nanachi Inc. Built with Docusaurus.`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          routeBasePath: '/',
          editUrl:
            'https://github.com/takesei/tech-stats/edit/master/website/'
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
