# codegen.py: code generator functions for wxStaticBitmap objects
# $Id: perl_codegen.py,v 1.2 2003/06/25 23:51:26 crazyinsomniac Exp $
#
# Copyright (c) 2002-2003 Alberto Griggio <albgrig@tiscalinet.it>
# License: MIT (see license.txt)
# THIS PROGRAM COMES WITH NO WARRANTY

import common, os

#this should be in common 
_bmp_str_types = {
    '.bmp' : 'wxBITMAP_TYPE_BMP',
    '.gif' : 'wxBITMAP_TYPE_GIF',
    '.xpm' : 'wxBITMAP_TYPE_XPM',
    '.jpg' : 'wxBITMAP_TYPE_JPEG',
    '.jpeg': 'wxBITMAP_TYPE_JPEG',
    '.png' : 'wxBITMAP_TYPE_PNG',
    '.pcx' : 'wxBITMAP_TYPE_PCX'
    }


class PerlCodeGenerator:
    def get_code(self, obj):
        init = []
        plgen = common.code_writers['perl']
        prop = obj.properties

        attribute = plgen.test_attribute(obj)

        id_name, id = plgen.generate_code_id(obj) 

        if not obj.parent.is_toplevel:
            parent = '$self->{%s}' % obj.parent.name
        else:
            parent = '$self'

        bmp_file = prop.get('bitmap', '')
        if not bmp_file:
            bmp = 'wxNullBitmap'
        else:
            type = _bmp_str_types.get(os.path.splitext(bmp_file)[1].lower())
            if not type:
                bmp = 'wxNullBitmap'
            else:
                bmp = 'Wx::Bitmap->new(%s, %s)' % \
                      (plgen.quote_str(bmp_file), type)

        if id_name: init.append(id_name)
        if attribute:
            prefix = '$self->{%s}' % obj.name
        else:
            prefix = '$self'

        style = prop.get('style')
        if not style: style = ''

        init.append('%s = %s->new(%s, %s, %s,%s);\n' % 
            (prefix, obj.klass.replace('wx','Wx::',1), parent, id, bmp, style))
        props_buf = plgen.generate_common_properties(obj)

        if not attribute:
            # the object doesn't have to be stored as an attribute of the
            # custom class, but it is just considered part of the layout
            return [], [], init + props_buf
        return init, props_buf, []

# end of class PerlCodeGenerator


def initialize():
    common.class_names['EditStaticBitmap'] = 'wxStaticBitmap'

    plgen = common.code_writers.get('perl')
    if plgen:
        plgen.add_widget_handler('wxStaticBitmap', PerlCodeGenerator())