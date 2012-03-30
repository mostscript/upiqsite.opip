#

import logging
import os

from Products.CMFCore.utils import getToolByName

from config import PathConfig


logger = logging.getLogger('')


def enable_smtp_queue(context):
    """
    This used to be designed to work around: https://bugs.launchpad.net/zope-cmf/+bug/602989
    
    ...however, now the primary reason this is used in lieu of setup XML
    is that this can set up the maildir directories if missing.
    
    Call from import_steps.xml.
    
    This also creates proper maildir format directory within the site
    buildout var/mailqueue directory.  The queue processor thread will
    not be started until the first message is sent, so we avoid trying
    to start the thread here after configuration, it doesn't buy us much.
    """
    mailhost = getToolByName(context, 'MailHost')
    if 'smtp_queue' in mailhost.__dict__:
        mailhost.smtp_queue = True
        pc = PathConfig()
        vardir = pc.get('var', os.path.join(pc.get('buildout',''), 'var'))
        maildir = os.path.join(vardir, 'mailqueue')
        if not os.path.exists(maildir):
            os.mkdir(maildir)
            logger.info('Created mail queue directory: %s' % maildir)
        for subdir in ('tmp', 'new', 'cur'):
            p = os.path.join(maildir, subdir)
            if not os.path.exists(p):
                os.mkdir(p)
            logger.info('Created maildir subdirectory:\n\t%s' % p)
        mailhost.smtp_queue_directory = maildir

