  // Generate margins paddings & other spaces tailwindcss classes
 
  // @param {number} [m=5] module width
  // @param {number} [c=50] module max steps
  // @return {array} array for tailwind config
 
  const generateSpacing = (m = 5, c = 150) => {
    const result = {}
  
    for (let i = c; i >= 0; i--) {
      const r = i * m
      result[r] = `${r}px`
    }
  
    return result
  }
  
  module.exports = {
    purge: [],
    darkMode: false, 
    theme: {
      spacing: generateSpacing(),
  
      colors: {
        transparent: 'transparent',
        black: '#000000',
        white: '#ffffff',
        // blur: 'rgba(255, 255, 255, 0.08);',
        // Заголовки и кнопки
        one: '#111111',
        // Подзаголовки
        one: '#9C9C9B',
        // Текст и активное меню
        three: '#333333',
        // Неактивное меню
        four: '#7F7F7F',

        blue: '#0091FA',
      },
      fontSize: {
        'fxs': ['12px', {lineHeight: '100%'}],
        'subtwo': ['14px', {lineHeight: '132%'}],
        'caption': ['16px', {lineHeight: '120%'}],
        'body': ['18px', {lineHeight: '132%'}],
        'subone': ['24px', {lineHeight: '120%'}],
        'h4': ['36px', {lineHeight: '120%'}],
        'h3': ['48px' , {lineHeight: '100%'}],
        'h2': ['72px' , {lineHeight: '100%'}],
        'h1': ['96px', {lineHeight: '100%'}],
      },
      opacity: {
        '0': '0',
        '10': '0.1',
        '15': '0.15',
        '25': '0.25',
        '30': '0.3',
        '50': '0.5',
        '75': '0.75',
        '100': '1',
      },
      screens: {
        'sxs': '375px',
        'ss': '420px',
        'sm': '565px',
        'sl': '770px',
        'slx': '1400px',
      },
  
  
      extend: {},
    },
    variants: {
      extend: {},
    },
    plugins: [],
  }
  