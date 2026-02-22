Install:

Windows:
python -m venv .venv
.\.venv\Scripts\activate

Mac:
python3 -m venv .venv
source .venv/bin/activate

1. pip install -r requirement.txt
		OR
2. Manual:
pip install fastapi
pip install uvicorn
pip install pydantic
pip install openai
pip install python-dotenv
pip install pillow
pip install python-multipart

Note: All packages ae present in requirement.txt, you can direct run 1st command or run all manually.

Add API key in .env : OPENAI_API_KEY=your_api_key_here
How to run?

1. Run uvicorn main:app --reload in VS code terminal.
2. You will see "Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)" copy this URL from terminal and run on browser.
3. Append /docs to URL on browser to open swagger.
4. On swagger you will see, POST method /generate, click on try it out.
5. In request body, add input data: 

Sample input data: 

{
  "username": "ABC",
  "platform": "instagram",
  "company": "SUGAR",
  "event": "New Skincare Launch Campaign",
  "title": "Glow That Speaks.",
  "product_description": "A premium skincare range designed to hydrate, brighten, and enhance natural glow with dermatologist-tested ingredients suitable for all skin types.",
  "num_images": 3,
  "num_captions": 4,
  "brand_name": "SUGAR",
  "color": "soft peach, nude pink, and warm beige tones with subtle glow highlights",
  "want_images": false,
  "want_captions": true,
  "Target_audience": "Women aged 18-35 who love modern beauty trends, skincare enthusiasts, and urban professionals",
  "Product": "Hydrating serum and glow-enhancing skincare collection",
  "Style": "modern beauty brand aesthetic, bold yet elegant, clean luxury skincare visuals",
  "campaign_message": "Hydrate. Glow. Repeat.",
  "features": [
    "Deep Hydration Formula",
    "Vitamin C Glow Boost",
    "Dermatologist Tested",
    "Suitable for All Skin Types"
  ],
  "layout": "premium product-focused composition with close-up skincare bottle, soft lighting, smooth textured background, subtle beauty aesthetic",
  "mood": "confident, radiant, fresh, luxurious",
  "call_to_action": "Shop Now"
}

6. Generated images are saved in a generated_images/username folder in the project directory .

7. Captions will appear in Swagger under Response Body

8. To run UI, open a seperate terminal and run streamlit run app.py

Note: To run both backend and frontend together run both streamlit run app.py and uvicorn main:app in seperate terminals.

