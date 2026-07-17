import { describe, it, expect } from 'vitest';

import { render, screen } from '../../test/utils/test-utils';

import Page from '@/app/page';

describe('App', () => {
  it('should render the landing page', () => {
    render(<Page />);
    expect(screen.getByText(/Architecture Status/i)).toBeInTheDocument();
  });
});
