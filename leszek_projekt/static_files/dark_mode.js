function setCSSVariables() {
  if (localStorage.getItem('darkMode') === 'true') {
    // Set dark mode variables
    const root = document.documentElement;
    root.style.setProperty('--background-color', '#262b2c');
    root.style.setProperty('--on-background-color', '#414546');
    root.style.setProperty('--on-on-background-color', '#585e5f');
    root.style.setProperty('--primary-color', '#006a71');
    root.style.setProperty('--secondary-color', '#31797f');
    root.style.setProperty(
      '--gradient-light',
      'linear-gradient(#161c1d, #262b2c)'
    );
    root.style.setProperty('--header', '#151a1b');
    root.style.setProperty('--light-text', '#fbfbfe');
    root.style.setProperty('--dark-text', '#fbfbfe');
  } else if (localStorage.getItem('darkMode') === 'false') {
    // Set light mode variables
    const root = document.documentElement;
    root.style.setProperty('--background-color', '#fbfbfe');
    root.style.setProperty('--header', '#fbfbfe');
    root.style.setProperty('--on-background-color', '#fcfcff');
    root.style.setProperty('--primary-color', '#006a71');
    root.style.setProperty('--secondary-color', '#48a6a7');
    root.style.setProperty(
      '--gradient-light',
      'linear-gradient(#eef6f7, #9acbd0)'
    );
    root.style.setProperty('--light-text', '#fbfbfe');
    root.style.setProperty('--dark-text', '#040316');

    // Unset dark-only vars
    root.style.removeProperty('--on-on-background-color');
  }
}
