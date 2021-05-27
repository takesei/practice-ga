/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: 'Sample Tech Stats Website',
  tagline: 'Dinosaurs are cool',
  url: 'https://takesei.github.io',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'takesei', // Usually your GitHub org/user name.
  projectName: 'tech-stats', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'My Site',
      hideOnScroll: true,
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'tutorials/intro',
          position: 'left',
          label: 'Tutorial',
        },
        {
          type: 'doc',
          docId: 'subetedoc/intro',
          position: 'left',
          label: 'Subete Doc',
        },
        {
          label: 'Blog',
          position: 'left',
          items: [
            {
              label: 'Yurufuwa Blog',
              to: 'blog'
            },
            {
              label: 'Tech Blog',
              to: 'blog',
            }
          ],
        },
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
          title: 'Docs',
          items: [
            {
              label: 'Tutorial',
              to: 'blog',
            },
          ],
        },
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
              label: 'Yurufuwa Blog',
              to: 'blog',
            },
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
          routeBasePath: 'docs',
          editUrl:
            'https://github.com/facebook/docusaurus/edit/master/website/',
        },
        blog: {
          id: "preset-classic-1",
          showReadingTime: true,
          id: 'blog',
          path: "./blog/yurufuwablog",
          routeBasePath: 'blog',
          // Please change this to your repo.
          editUrl:
          'https://github.com/facebook/docusaurus/edit/master/website/blog/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
    [
      '@docusaurus/plugin-content-blog',
      {
        showReadingTime: true,
        id: 'techblog',
        path: "./blog/techblopg",
        routeBasePath: 'techblog',
        // Please change this to your repo.
        editUrl:
        'https://github.com/facebook/docusaurus/edit/master/website/blog/',
      },
    ],
  ],
};
