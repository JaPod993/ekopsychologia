module.exports = function (grunt) {
    grunt.initConfig({
        wiredep: {
            task: {
                ignorePath: '../../../../static/',
                src: [
                    'ekopsychologia/apps/website/templates/website/site/base/layout.html'
                ],
                fileTypes: {
                    html: {
                        replace: {
                            js: '<script src="{% static \'{{filePath}}\' %}"></script>',
                            css: '<link rel="stylesheet" href="{% static \'{{filePath}}\' %}" />'
                        }
                    }
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-wiredep');
    grunt.loadNpmTasks('grunt-preen');
    grunt.registerTask('default', ['preen', 'wiredep']);
};