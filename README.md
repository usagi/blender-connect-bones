# blender-connect-bones

Blender add-on: Connect bones if it find a bone pair that has a same position of a head and a tail

Note: 日本語参考 → <https://usagi.hatenablog.jp/entry/2020/04/12/110722>

## Feature

1. Make a `Connected` parent-child bone pair(s) automatically.
2. With REGEX pattern filtering, head-tail position tolerance( distance absolute ).
3. Keyboardshortcut `CTRL + SHIFT + ALT + C` in `3D View` -> REGEX dialogue -> Execute!
4. Or, `bpy.ops.armature.connect_bones( name_regex = 'Neko' )` in `Python Console` -> Execute!

## Screenshot

<table>
  <tr>
    <td><img src="https://i.imgur.com/3vEynpK.png" /> <p>*Before*; There were unfortunately disconnected many bones.</p>
    <td><img src="https://i.imgur.com/p9Wj13e.png" /> <p>*After*; There are connected!</p>
  </tr>
  <tr>
    <td><img src="https://i.imgur.com/Pdw2S54.png" /> <p>Use the add-on with the keyboard shortcut `CTRL + SHIFT + ALT + C` then you can use the regex filter pattern dialogue.</p>
    <td><img src="https://i.imgur.com/iW2qdTy.png" /> <p>Use the add-on with the `Python Console` feature.</p>
  </tr>
</table>

And more screenshots here: <https://imgur.com/a/MPvVNyq>

## LICENSE

[MIT](LICENSE)

## Author

USAGI.NETWORK / Usagi Ito <https://usagi.network/>
