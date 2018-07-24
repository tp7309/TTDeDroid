/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  android.os.Bundle
 *  android.view.View
 *  com.meituan.robust.ChangeQuickRedirect
 *  com.meituan.sample.SecondActivity
 */
package com.meituan.robust.patch;

import android.os.Bundle;
import android.view.View;
import com.meituan.robust.ChangeQuickRedirect;
import com.meituan.robust.patch.SecondActivityPatch;
import com.meituan.sample.SecondActivity;
import java.util.Map;
import java.util.WeakHashMap;

public class SecondActivityPatchControl
implements ChangeQuickRedirect {
    public static final String MATCH_ALL_PARAMETER = "(\\w*\\.)*\\w*";
    private static final Map<Object, Object> keyToValueRelation = new WeakHashMap<Object, Object>();

    /*
     * Enabled aggressive block sorting
     * Enabled unnecessary exception pruning
     * Enabled aggressive exception aggregation
     */
    public Object accessDispatch(String string, Object[] arrobject) {
        try {
            SecondActivityPatch secondActivityPatch;
            if (string.split(":")[2].equals("false")) {
                if (keyToValueRelation.get(arrobject[arrobject.length - 1]) == null) {
                    secondActivityPatch = new SecondActivityPatch(arrobject[arrobject.length - 1]);
                    keyToValueRelation.put(arrobject[arrobject.length - 1], secondActivityPatch);
                } else {
                    secondActivityPatch = (SecondActivityPatch)keyToValueRelation.get(arrobject[arrobject.length - 1]);
                }
            } else {
                secondActivityPatch = new SecondActivityPatch(null);
            }
            if ("89".equals(string = string.split(":")[3])) {
                secondActivityPatch.onCreate((Bundle)arrobject[0]);
            }
            if ("90".equals(string)) {
                return secondActivityPatch.getTextInfo((Object[])arrobject[0]);
            }
            if (!"100".equals(string)) return null;
            secondActivityPatch.RobustPubliclambda$onCreate$0((View)arrobject[0]);
            return null;
        }
        catch (Throwable throwable) {
            throwable.printStackTrace();
        }
        return null;
    }

    public Object getRealParameter(Object object) {
        Object object2 = object;
        if (object instanceof SecondActivity) {
            object2 = new SecondActivityPatch(object);
        }
        return object2;
    }

    public boolean isSupport(String string, Object[] arrobject) {
        return "89:90:100:".contains(string.split(":")[3]);
    }
}

