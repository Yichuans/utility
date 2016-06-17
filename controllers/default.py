# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def wh_pic_redirect():
    response.headers['Access-Control-Allow-Origin'] = '*'
    args = request.args

    if args:
        wdpaid = args[0]
        # redirect(URL('static','images/test.jpg'))
        return response.stream(URL('static','images/test.jpg'))
    else:
        return None


def wh_pic():
    response.headers['Access-Control-Allow-Origin'] = '*'
    args = request.args

    if args:
        wdpaid = args[0]

        import os
        # the URL function won't work
        path = os.path.join(request.folder, 'static', 'images', 'test.jpg')

        # if not found
        if not os.path.exists(path):
            path = ''

        return response.stream(path)
    else:
        return None

def test_stream():
    import os
    path = os.path.join(request.folder, 'static', 'images', 'test.jpg')
    # return path
    return response.stream(path) 

        # return response.stream()

def wh_pic_url():
    response.headers['Access-Control-Allow-Origin'] = '*'
    args = request.args

    if args:
        wdpaid = args[0]
        return URL('static','images/test.jpg')
    else:
        return None

def wh_attr():
    response.headers['Access-Control-Allow-Origin'] = '*'
    import json

    args = request.args
    if args:
        wdpaid = args[0]
        row = db(db.wh.wdpaid == wdpaid).select()[0].as_dict()
    else:
        row = {}

    return json.dumps(row)

def wh_all():
    from utility import get_all_wh

    wh = get_all_wh().as_list()

    import json

    return json.dumps(wh)
