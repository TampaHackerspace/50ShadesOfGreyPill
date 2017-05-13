#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This is a stripped down of th Google Detect Example code
# located @ https://github.com/GoogleCloudPlatform

import argparse
import io

from google.cloud import vision

def report(annotations):
    """Prints detected features in the provided web annotations."""
    if annotations.pages_with_matching_images:
        print('\nPages with matching images retrieved')
        for page in annotations.pages_with_matching_images:
            print('Url   : {}'.format(page.url))

    if annotations.full_matching_images:
        print ('\n{} Full Matches found: '.format(len(annotations.full_matching_images)))
        for image in annotations.full_matching_images:
            print('Url  : {}'.format(image.url))

    if annotations.partial_matching_images:
        print ('\n{} Partial Matches found: '.format(len(annotations.partial_matching_images)))
        for image in annotations.partial_matching_images:
            print('Url  : {}'.format(image.url))

    if annotations.web_entities:
        print ('\n{} Web entities found: '.format(len(annotations.web_entities)))
        for entity in annotations.web_entities:
            print('Score      : {}'.format(entity.score) + ' | Description: {}'.format(entity.description))


def detect_text(path):
    """Detects text in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    texts = image.detect_text()
    print('Texts:')

    for text in texts:
        print((text.description))

        #vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
        #            for bound in text.bounds.vertices])
	#
        #print('bounds: {}'.format(','.join(vertices)))

    report(image.detect_web())




def run_local(args):
    if args.command == 'text':
        detect_text(args.path)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    detect_text_parser = subparsers.add_parser('text', help=detect_text.__doc__)
    detect_text_parser.add_argument('path')

    args = parser.parse_args()

    if ('uri' in args.command):
        run_uri(args)
    else:
        run_local(args)
