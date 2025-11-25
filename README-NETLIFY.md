# 🏰 Disney Trip Planner - Royal Princess Edition

> A professional, elegant HTML/CSS/JavaScript site for planning magical Disney vacations

## ✨ Features

- **Royal Princess Theme**: Elegant design with lavenders, pinks, and golds
- **Multi-User Collaboration**: Share trip codes with family and friends
- **AI-Powered**: Smart checklist generation and trip suggestions
- **Fully Responsive**: Beautiful on all devices
- **Local Storage**: Your data is saved automatically
- **Professional Design**: Built with modern web standards

## 🚀 Deploy to Netlify

### Quick Deploy

1. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Add Netlify HTML site"
   git push origin your-branch-name
   ```

2. **Deploy to Netlify**:
   - Go to [app.netlify.com](https://app.netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Connect to GitHub and select this repository
   - Configure build settings:
     - **Build command**: Leave empty (static site)
     - **Publish directory**: `public`
   - Click "Deploy site"

3. **Configure Environment Variables** (Optional - for future AI features):
   - Go to Site settings → Environment variables
   - Add: `OPENAI_API_KEY` = your OpenAI API key

### Local Development

To run locally:

```bash
# Option 1: Python HTTP Server
python3 -m http.server 8000 --directory public

# Option 2: Any other local server
# Then open http://localhost:8000
```

## 📁 Project Structure

```
Disney Agent/
├── public/                 # Static files (published to web)
│   ├── index.html         # Main HTML file
│   ├── css/
│   │   └── styles.css     # Royal princess theme CSS
│   ├── js/
│   │   └── app.js         # Application logic
│   └── assets/
│       └── images/        # Images (add favicon, etc.)
├── netlify/
│   └── functions/         # Serverless functions (future)
├── netlify.toml           # Netlify configuration
├── package.json           # Project metadata
└── README-NETLIFY.md      # This file
```

## 🎨 Design System

### Colors
- **Royal Purple**: #8B5FBF
- **Soft Lavender**: #B8A4D9
- **Blush Pink**: #FFB6C1
- **Rose Gold**: #B76E79
- **Gold**: #D4AF37

### Typography
- **Headings**: Playfair Display (elegant serif)
- **Special Text**: Cormorant Garamond (classic serif)
- **Body**: Montserrat (clean sans-serif)

## 💾 Data Storage

Currently uses **localStorage** for data persistence:
- Each trip is saved with a unique trip code
- Data persists across browser sessions
- Share trip codes with family members

### Future Enhancements
- Cloud sync with Firebase
- Real-time collaboration
- AI-powered suggestions via OpenAI

## 🛠️ Customization

### Change Colors
Edit `public/css/styles.css` and update the CSS variables in the `:root` section.

### Add Custom Features
Modify `public/js/app.js` to add new functionality.

### Enable AI Features
Create Netlify Functions in `netlify/functions/` to integrate with OpenAI API.

## 📱 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 🎯 Next Steps

1. **Add your own branding**: Update colors, fonts, and text
2. **Add images**: Place logo and images in `public/assets/images/`
3. **Enable AI**: Set up Netlify Functions for OpenAI integration
4. **Custom domain**: Configure a custom domain in Netlify settings

## 📄 License

MIT License - Feel free to use and modify!

---

✨ **Built with magic and love for Disney families** ✨
