{
  "targets": [
    {
      "target_name": "geos",
      "sources": [
        "src/cpp/binding.cpp",
        "src/cpp/geometry.cpp",
        "src/cpp/wktreader.cpp",
        "src/cpp/wkbreader.cpp",
        "src/cpp/wktwriter.cpp",
        "src/cpp/wkbwriter.cpp",
        "src/cpp/geometryfactory.cpp",
        "src/cpp/precisionmodel.cpp",
        "src/cpp/geojsonwriter.cpp",
        "src/cpp/geojsonreader.cpp"
      ],
      'cflags!': [ '-fno-exceptions', '-fno-rtti' ],
      'cflags_cc!': [ '-fno-exceptions', '-fno-rtti' ],
      'conditions': [
        ['OS=="win"', {
          "defines": [
            "round=floor"
          ],
          'libraries': [
            "geos.lib"
          ],
          'configurations': {
            'Release': {
              'msvs_settings': {
                'VCCLCompilerTool': {
                  'RuntimeLibrary': 2
                }
              }
            }
          }
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'MACOSX_DEPLOYMENT_TARGET': '10.8',
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'GCC_ENABLE_CPP_RTTI': 'YES',
            'OTHER_CFLAGS': [
              '<!@(geos-config --cflags)'
            ]
          }
        }],
        ['OS=="linux"', {
          'cflags': [
            '<!@(geos-config --cflags)'
          ],
          'libraries': [
            '<!@(geos-config --libs)'
          ]
        }]
      ]
    }
  ]
}
