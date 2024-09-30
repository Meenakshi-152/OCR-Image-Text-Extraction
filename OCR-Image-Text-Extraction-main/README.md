# OCR-Image-Text-Extraction

Description:
This project combines Optical Character Recognition (OCR) and keyword search functionality to extract text from images and then search for specific terms within the extracted text.

Features:

OCR functionality: Leverages the Qwen2VL model for accurate text extraction from images.

Keyword search: Enables users to search for specific keywords within the extracted text, highlighting the matches.

Installation:
Install required dependencies:
pip install gradio transformers


Usage:
Start the Gradio app by running python app.py (replace app.py with your actual file name if different).
OCR Image Text Extraction:
Upload an image using the image input component.
Click "Run" to process the image.
The extracted text will be displayed in the output textbox.
Keyword Search:
Paste the extracted text from the OCR interface or enter your own text in the first text input.
Enter a keyword or phrase to search for in the second text input.
Click "Run" to perform the search.
The output textbox will display the extracted text with matching keywords highlighted in bold.


Model:
Qwen2VLForConditionalGeneration: A pre-trained model from the Qwen/Qwen2-VL-2B-Instruct library is used for text extraction.

App link:
1) For Extraction: https://011470bf13d65c8e28.gradio.live
2) For Search: https://d003114c0efbe10d0b.gradio.live
