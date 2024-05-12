describe('Jest framework readiness', () => {
  test('check jest ready', () => {
    expect(1 + 1).toBe(2);
  });

  it('should be a numberr', () => {
    expect(1).toBeTruthy();
  });
});
