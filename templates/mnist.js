class MNIST {

    getInfo() {
        return {
            id: 'mnist',
            name: 'MINST',
            blocks: [
                {
                    opcode: 'label',
                    blockType: Scratch.BlockType.REPORTER,
                    text: {
                        default: 'recognise image [IMAGE] (label)',
                        id: 'mlforkids.images.recogniseLabel'
                    },
                    arguments: {
                        IMAGE: {
                            type: Scratch.ArgumentType.STRING,
                            defaultValue: 'image'
                        }
                    }
                },
            ],
        };
    }

    label({ IMAGE }) {
        return new Promise(resolve => getImageClassificationResponse(IMAGE, resolve));
    }
}

function getImageClassificationResponse(imagedata, callback) {
    if (imagedata === '' || imagedata === 'image') {
        return callback('You need to put an image block in here');
    }

    var url = new URL('{{url_root}}' + 'mnist');

    var options = {
        headers : {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        method : 'POST',
        body : JSON.stringify({
            data : imagedata,
        })
    };

    fetch(url, options).then((response) => {
        if (response.status === 200 || response.status === 400) {
            response.json().then((responseJson) => {
                if (response.status === 200 && responseJson && responseJson.length > 0) {
                    // we got a result from the classifier
                    return callback(responseJson[0]);
                }

                callback({
                    class_name: 'Unknown',
                    confidence: 0,
                });
            });
        }
        else {
            console.log(response);

            callback({
                class_name: 'Unknown',
                confidence: 0,
            });
        }
    })
    .catch((err) => {
        console.log(err);

        callback({
            class_name: 'Unknown',
            confidence: 0,
        });
    });
}

Scratch.extensions.register(new MNIST());