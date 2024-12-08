'use client'

import { useAuth } from '@/hooks/useAuth'
import {
  Bars3Icon,
  HomeIcon,
  ShoppingBagIcon,
  UserGroupIcon,
  CalculatorIcon,
  ChartBarIcon,
} from '@heroicons/react/24/outline'
import { cn } from '@/lib/utils'
import Link from 'next/link'
import { usePathname } from 'next/navigation'

const navigation = [
  { name: 'Dashboard', href: '/dashboard', icon: HomeIcon },
  { name: 'Inventory', href: '/dashboard/inventory', icon: ShoppingBagIcon },
  { name: 'Customers', href: '/dashboard/customers', icon: UserGroupIcon },
  { name: 'Billing', href: '/dashboard/billing', icon: CalculatorIcon },
  { name: 'Reports', href: '/dashboard/reports', icon: ChartBarIcon },
]

interface Props {
  setSidebarOpen: (open: boolean) => void
}

export function DashboardNav({ setSidebarOpen }: Props) {
  const pathname = usePathname()
  const { user } = useAuth()

  return (
    <div className="sticky top-0 z-40 flex h-16 shrink-0 items-center gap-x-4 border-b border-gray-200 bg-white px-4 shadow-sm sm:gap-x-6 sm:px-6 lg:px-8">
      <button
        type="button"
        className="-m-2.5 p-2.5 text-gray-700 lg:hidden"
        onClick={() => setSidebarOpen(true)}
      >
        <span className="sr-only">Open sidebar</span>
        <Bars3Icon className="h-6 w-6" aria-hidden="true" />
      </button>

      {/* Separator */}
      <div className="h-6 w-px bg-gray-200 lg:hidden" aria-hidden="true" />

      <div className="flex flex-1 gap-x-4 self-stretch lg:gap-x-6">
        <div className="flex flex-1">
          {/* Navigation */}
          <nav className="flex space-x-4 lg:space-x-8">
            {navigation.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className={cn(
                  pathname === item.href
                    ? 'text-primary-600'
                    : 'text-gray-700 hover:text-primary-600',
                  'group flex items-center gap-x-3 rounded-md p-2 text-sm font-semibold leading-6'
                )}
              >
                <item.icon
                  className={cn(
                    pathname === item.href
                      ? 'text-primary-600'
                      : 'text-gray-400 group-hover:text-primary-600',
                    'h-6 w-6 shrink-0'
                  )}
                  aria-hidden="true"
                />
                <span className="hidden lg:block">{item.name}</span>
              </Link>
            ))}
          </nav>
        </div>
        <div className="flex items-center gap-x-4 lg:gap-x-6">
          {/* Profile dropdown */}
          <div className="relative">
            <span className="inline-flex h-8 w-8 items-center justify-center rounded-full bg-primary-100">
              <span className="text-sm font-medium leading-none text-primary-700">
                {user?.first_name?.[0]}
                {user?.last_name?.[0]}
              </span>
            </span>
          </div>
        </div>
      </div>
    </div>
  )
}
