import type { Metadata, Viewport } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'AHS Accessibility Visualization',
  description:
    'Interactive visualization of accessibility features in the U.S. housing stock based on the 2019 American Housing Survey.',
  icons: {
    icon: '/vite.svg',
  },
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
