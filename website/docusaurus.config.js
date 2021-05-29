/** @type {import('@docusaurus/types').DocusaurusConfig} */

const fs = require('fs');

const getDocsDirs = () => {
  return fs.readdirSync('./docs', { withFileTypes: true })
    .flatMap(d => d.isFile() ? null: d.name)
    .filter(v => v !== null);
}


module.exports = {
  title: 'Sample Tech Stats Website',
  tagline: 'Dinosaurs are cool',
  url: 'https://takesei.github.io',
  baseUrl: '/tech-stats',
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
      title: 'My Site',
      hideOnScroll: true,
      logo: {
        alt: 'My Site Logo',
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
          href: 'https://github.com/facebook/docusaurus',
          label: 'GitHub',
          position: 'right',
        },
        {
          type: 'search',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/docusaurus',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/facebook/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
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
            'https://github.com/facebook/docusaurus/edit/master/website/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
