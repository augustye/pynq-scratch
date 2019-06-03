class Scratch3NewBlocks {
    constructor (runtime) {
        this.runtime = runtime;
    }

    getInfo () {
        return {
            id: 'newblocks',
            name: 'New Blocks',
            blocks: [
                {
                    opcode: 'ledControl',
                    blockType: Scratch.BlockType.COMMAND,
                    text: 'led [STATUS]',
                    arguments: {
                        STATUS: {
                            type: Scratch.ArgumentType.STRING,
                            defaultValue: "0",
                            menu: 'statuses'
                        }
                    }
                }
            ],
            menus: {
                statuses: [
                    { value : '0', text : 'off'},
                    { value : '1', text : 'on' },
                ]
            }
        };
    }

    ledControl({ STATUS }) {
        return new Promise(resolve => sendLedCommand(STATUS, resolve));
    }
}

function sendLedCommand(status, callback) {
    var url = new URL('http://127.0.0.1:8888/led');
    url.searchParams.append('status', status);
    fetch(url).then((response) => {
        console.log("sendLedCommand response:", response);
        return callback(response);
    })
}

Scratch.extensions.register(new Scratch3NewBlocks());