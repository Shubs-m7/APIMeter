import type { Metadata } from 'next';
import { Inter } from 'next/font/google';

import './globals.css';
import { APP_CONSTANTS } from '@/constants/app';
import { Providers } from '@/providers/providers';

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });

export const metadata: Metadata = {
  title: {
    default: APP_CONSTANTS.TITLE,
    template: `%s | ${APP_CONSTANTS.TITLE}`,
  },
  description: APP_CONSTANTS.DESCRIPTION,
  openGraph: {
    title: APP_CONSTANTS.TITLE,
    description: APP_CONSTANTS.DESCRIPTION,
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: APP_CONSTANTS.TITLE,
    description: APP_CONSTANTS.DESCRIPTION,
  },
  icons: {
    icon: '/favicon.ico',
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${inter.variable} antialiased min-h-screen bg-background text-foreground`}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
