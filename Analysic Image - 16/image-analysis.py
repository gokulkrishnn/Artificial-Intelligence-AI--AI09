from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
import sys
from matplotlib import pyplot as plt
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential


def main():

    # Clear console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Load ENV config
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Get image file argument
        image_file = 'images/street.jpg'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        # Instantiate Azure Vision Client
        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )

        # Read image
        with open(image_file, "rb") as f:
            image_data = f.read()

        print(f'\nAnalyzing {image_file}\n')

        # Call model
        result = cv_client.analyze(
            image_data=image_data,
            visual_features=[
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
                VisualFeatures.PEOPLE
            ],
        )

        # -----------------------------
        # CAPTIONS
        # -----------------------------
        if result.caption is not None:
            print("\nCaption:")
            print(" Caption: '{}' (confidence: {:.2f}%)".format(
                result.caption.text,
                result.caption.confidence * 100
            ))

        if result.dense_captions is not None:
            print("\nDense Captions:")
            for caption in result.dense_captions.list:
                print(" Caption: '{}' (confidence: {:.2f}%)".format(
                    caption.text,
                    caption.confidence * 100
                ))

        # -----------------------------
        # TAGS
        # -----------------------------
        if result.tags is not None:
            print("\nTags:")
            for tag in result.tags.list:
                print(" Tag: '{}' (confidence: {:.2f}%)".format(
                    tag.name,
                    tag.confidence * 100
                ))

        # -----------------------------
        # OBJECTS
        # -----------------------------
        if result.objects is not None:
            print("\nObjects in image:")
            for obj in result.objects.list:
                print(" {} (confidence: {:.2f}%)".format(
                    obj.tags[0].name,
                    obj.tags[0].confidence * 100
                ))

            show_objects(image_file, result.objects.list)

        # -----------------------------
        # PEOPLE
        # -----------------------------
        if result.people is not None:
            print("\nPeople in image:")
            for person in result.people.list:
                if person.confidence > 0.2:
                    print(" {} (confidence: {:.2f}%)".format(
                        person.bounding_box,
                        person.confidence * 100
                    ))

            show_people(image_file, result.people.list)

    except Exception as ex:
        print("Error:", ex)


# -------------------------------------------------------------------
# DRAW OBJECTS
# -------------------------------------------------------------------
def show_objects(image_filename, detected_objects):
    print("\nAnnotating objects...")

    image = Image.open(image_filename)
    fig = plt.figure(figsize=(image.width / 100, image.height / 100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    for obj in detected_objects:
        r = obj.bounding_box
        box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
        draw.rectangle(box, outline=color, width=3)
        plt.annotate(obj.tags[0].name, (r.x, r.y), backgroundcolor=color)

    plt.imshow(image)
    plt.tight_layout(pad=0)
    output_file = 'objects.jpg'
    fig.savefig(output_file)
    print("  Results saved in", output_file)


# -------------------------------------------------------------------
# DRAW PEOPLE
# -------------------------------------------------------------------
def show_people(image_filename, detected_people):
    print("\nAnnotating people...")

    image = Image.open(image_filename)
    fig = plt.figure(figsize=(image.width / 100, image.height / 100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    for p in detected_people:
        if p.confidence > 0.2:
            r = p.bounding_box
            box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
            draw.rectangle(box, outline=color, width=3)

    plt.imshow(image)
    plt.tight_layout(pad=0)
    output_file = 'people.jpg'
    fig.savefig(output_file)
    print("  Results saved in", output_file)


if __name__ == "__main__":
    main()
